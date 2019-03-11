from flask import url_for,render_template,flash,redirect,request
import os
from jobber import app,db,bcrypt
from jobber.models import Employee
from flask_login import login_user,current_user,logout_user,login_required
from jobber.forms import EmployeeUpdateAccountForm,EmployeeRegistrationForm,EmployeeLoginForm,EmployerRegistrationForm,EmployerLoginForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/employee/register", methods=['GET', 'POST'])
def employeeregister():
    if current_user.is_authenticated:
        flash(f'Already Logged In')
        return redirect(url_for('home'))
    form=EmployeeRegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=Employee(name=form.name.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created')
        return redirect(url_for('employeelogin'))
    return render_template('employeeRegister.html',title='Employee Register',form=form)

@app.route("/employee/login", methods=['GET', 'POST'])
def employeelogin():
    if current_user.is_authenticated:
        flash(f'Already Logged In')
        return redirect(url_for('home'))
    form=EmployeeLoginForm()
    if form.validate_on_submit():
        user=Employee.query.filter_by(email=form.email.data).first()
        if(user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            flash(f'{user.name} Logged in')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Incorrect Log in')
    return render_template('employeeLogin.html',title='Employee Login',form=form)

@app.route("/employer/register", methods=['GET', 'POST'])
def employerregister():
    form=EmployerRegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created')
        return redirect(url_for('home'))
    return render_template('employerRegister.html',title='Employer Register',form=form)

@app.route("/employer/login", methods=['GET', 'POST'])
def employerlogin():
    form=EmployerLoginForm()
    return render_template('employerLogin.html',title='Employer Login',form=form)

@app.route("/logout")
def logout():
    if(current_user.is_authenticated):
        logout_user()
        flash(f'User Logged Out')
    else:
        flash(f'Log In First')
    return redirect(url_for('home'))

def save_picture(pic):
    _,f_ext=os.path.splitext(pic.filename)
    picture_fn=current_user.email+f_ext
    picture_path=os.path.join(app.root_path,'static/profile_pics',picture_fn)
    pic.save(picture_path)
    return picture_fn

@app.route("/employee/account", methods=['GET', 'POST'])
@login_required
def employeeaccount():
    form=EmployeeUpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn=save_picture(form.picture.data)
            current_user.profile_picture=picture_fn
            db.session.commit()
        if not (current_user.email==form.email.data and current_user.name==form.name.data):
            current_user.email=form.email.data
            current_user.name=form.name.data
            db.session.commit()
            flash(f'Account Updated')
            return redirect(url_for('employeeaccount'))
    elif request.method=='GET':
        form.email.data=current_user.email
        form.name.data=current_user.name
    return render_template('employeeAccount.html',title='Employee Account',form=form)