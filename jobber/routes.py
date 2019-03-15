from flask import url_for,render_template,flash,redirect,request
import os
from PIL import Image
from jobber import app,db,bcrypt
from jobber.models import User
from flask_login import login_user,current_user,logout_user,login_required
from jobber.forms import EmployeeUpdateAccountForm,EmployeeRegistrationForm,EmployeeLoginForm,EmployerRegistrationForm,EmployerLoginForm,EmployerUpdateAccountForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/employee/home")
def employeeHome():
    if current_user.is_authenticated and current_user.type=='employee':
        return render_template('employeeHome.html')
    elif current_user.is_authenticated and current_user.type=='employer':
        flash(f'Logged in as employer. Logout and log in as Employee')
        return redirect(url_for('employerHome'))
    elif not current_user.is_authenticated:
        flash(f'You need to log in first')
        return redirect(url_for('employeelogin'))

@app.route("/employer/home")
def employerHome():
    if current_user.is_authenticated and current_user.type=='employee':
        flash(f'Logged in as employee. Logout and log in as Employer')
        return redirect(url_for('employeeHome'))
    elif current_user.is_authenticated and current_user.type=='employer':
        return render_template('employerHome.html')
    elif not current_user.is_authenticated:
        flash(f'You need to log in first')
        return redirect(url_for('employerlogin'))

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/employee/register", methods=['GET', 'POST'])
def employeeregister():
    if current_user.is_authenticated:
        flash(f'Already Logged In')
        return redirect(url_for('employeeHome'))
    form=EmployeeRegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(name=form.name.data,email=form.email.data.lower(),password=hashed_password,type='employee')
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created')
        return redirect(url_for('employeelogin'))
    return render_template('employeeRegister.html',title='Employee Register',form=form)

@app.route("/employee/login", methods=['GET', 'POST'])
def employeelogin():
    if current_user.is_authenticated:
        if current_user.type=='employee':
            flash(f'Already Logged In')
            return redirect(url_for('employeeHome'))
        else:
            return redirect(url_for('employerHome'))
    form=EmployeeLoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data.lower()).first()
        if(user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            flash(f'{user.name} Logged in')
            return redirect(next_page) if next_page else redirect(url_for('employeeHome'))
        else:
            flash(f'Incorrect Log in')
    return render_template('employeeLogin.html',title='Employee Login',form=form)

@app.route("/employer/register", methods=['GET', 'POST'])
def employerregister():
    if current_user.is_authenticated:
        flash(f'Already Logged In')
        return redirect(url_for('employerHome'))
    form=EmployerRegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(name=form.name.data,email=form.email.data.lower(),password=hashed_password,type='employer',company_name=form.company_name.data,company_gst_number=form.company_gst_number.data,company_info=form.company_info.data,position=form.position.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Employer Account Created')
        return redirect(url_for('employerlogin'))
    return render_template('employerRegister.html',title='Employer Register',form=form)

@app.route("/employer/login", methods=['GET', 'POST'])
def employerlogin():
    if current_user.is_authenticated:
        flash(f'Already Logged In')
        return redirect(url_for('employerHome'))
    form=EmployerLoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data.lower()).first()
        if(user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            flash(f'{user.name} Logged in')
            return redirect(next_page) if next_page else redirect(url_for('employerHome'))
        else:
            flash(f'Incorrect Log in')
    return render_template('employerLogin.html',title='Employer Login',form=form)

    

@app.route("/logout")
def logout():
    if(current_user.is_authenticated):
        logout_user()
        flash(f'User Logged Out')
    else:
        flash(f'Log In First')
    return redirect(url_for('employeeHome'))

def save_picture(pic):
    _,f_ext=os.path.splitext(pic.filename)
    picture_fn=current_user.email+f_ext
    picture_path=os.path.join(app.root_path,'static/profile_pics',picture_fn)
    output_size=(125,125)
    i=Image.open(pic)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route("/employee/account", methods=['GET', 'POST'])
@login_required(role='employee')
def employeeaccount():
    form=EmployeeUpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn=save_picture(form.picture.data)
            current_user.profile_picture=picture_fn
            db.session.commit()
        if not (current_user.email==form.email.data.lower()):
            current_user.email=form.email.data.lower()
            current_user.name=form.name.data
            db.session.commit()
            flash(f'Account Updated')
            return redirect(url_for('employeeaccount'))
    elif request.method=='GET':
        form.email.data=current_user.email
        form.name.data=current_user.name
    return render_template('employeeAccount.html',title='Employee Account',form=form)

@app.route("/employer/account", methods=['GET', 'POST'])
@login_required(role='employer')
def employeraccount():
    form=EmployerUpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn=save_picture(form.picture.data)
            current_user.profile_picture=picture_fn
            db.session.commit()
        if not (current_user.email==form.email.data.lower()):
            current_user.email=form.email.data.lower()
            current_user.name=form.name.data
            current_user.company_name=form.company_name.data
            current_user.company_gst_number=form.company_gst_number.data
            current_user.company_info=form.company_info.data
            current_user.position=form.position.data
            db.session.commit()
            flash(f'Account Updated')
            return redirect(url_for('employeraccount'))
    elif request.method=='GET':
        form.email.data=current_user.email
        form.name.data=current_user.name
        form.company_name.data=current_user.company_name
        form.company_gst_number.data=current_user.company_gst_number
        form.company_info.data=current_user.company_info
        form.position.data=current_user.position
    return render_template('employerAccount.html',title='Employee Account',form=form)