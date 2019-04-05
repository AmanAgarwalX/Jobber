from flask import url_for,render_template,flash,redirect,request,jsonify,abort,make_response,request
import os
import time
from PIL import Image
from datetime import datetime
from jobber import app,db,bcrypt
from jobber.models import *
from flask_login import login_user,current_user,logout_user,login_required
from jobber.forms import *

@app.route("/")
@app.route("/home")
def home():
    page_num=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(per_page=2,page=page_num)
    return render_template('home.html',posts=posts)

@app.route("/employer/newjob",methods=['GET', 'POST'])
@login_required(role='employer')
def newjob():
    form=NewJobForm()
    if form.validate_on_submit():
        job=Job(title=form.title.data,location=form.location.data,typeofjob=form.typeofjob.data,salary=form.salary.data,description=form.description.data,user_id=current_user.id)
        db.session.add(job)
        db.session.commit()
        flash(f'New Job Created')
        return redirect(url_for('viewjob'))
    return render_template('newJobPage.html',title='New Job Form',form=form)


@app.route("/employer/jobs")
@login_required(role='employer')
def viewjob():
    return render_template('viewJobs.html',title='View Jobs',jobs=current_user.jobs,user=current_user.name)

@app.route("/employer/interviews/<job_id>")
@login_required(role='employer')
def viewinterviews(job_id):
    interviews=Job.query.get(job_id).interviews
    return render_template('viewinterviews.html',title='View Interviews for'+str(job_id),interviews=interviews)

@app.route("/employer/setinterview/<job_id>",methods=['GET', 'POST'])
@login_required(role='employer')
def setinterview(job_id):
    form=NewInterviewForm()
    if form.validate_on_submit():
        interview=Interview(title=form.title.data,location=form.location.data,time=datetime.combine(form.date.data,form.time.data),description=form.description.data,job=job_id)
        db.session.add(interview)
        db.session.commit()
        flash(f'New Interview Created')
        return redirect(url_for('viewinterviews',job_id=job_id))
    return render_template('setInterview.html',title='Set Interview Form',form=form,job_id=job_id)


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
        return redirect(url_for('employeeupdate'))
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

@app.route("/employee/update", methods=['GET', 'POST'])
@login_required(role='employee')
def employeeupdate():
    if current_user.is_authenticated:
        if current_user.type=='employee':
            form=EmployeeUpdateForm()
            if form.validate_on_submit():
                if form.picture.data:
                    picture_fn=save_picture(form.picture.data)
                    current_user.profile_picture=picture_fn
                    db.session.commit()
                if form.cv.data:
                    cv_fn=save_cv(form.cv.data)
                    current_user.cv=cv_fn
                    post = Post(title=current_user.name, content="upload", author=current_user)
                    db.session.add(post)
                    db.session.commit()
                    post.old_cv=cv_fn
                    db.session.commit()
                return redirect(url_for('employeeHome'))
            return render_template('employeeUpdate.html',title='Employee Update',form=form)
        else:
            return redirect(url_for('employerHome'))
    else:
        return redirect(url_for('employeeLogin'))

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

def save_cv(cv):
    _,f_ext=os.path.splitext(cv.filename)
    cv_fn=current_user.email+str(int(round(time.time() * 1000)))+f_ext
    cv_path=os.path.join(app.root_path,'static/cvs',cv_fn)
    cv.save(cv_path)
    return cv_fn


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

