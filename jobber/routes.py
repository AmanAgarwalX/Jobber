from flask import url_for,render_template,flash,redirect,request,jsonify,abort,make_response
import os
import time
from PIL import Image
from datetime import datetime
from jobber import app,db,bcrypt
from jobber.models import *
from flask_login import login_user,current_user,logout_user,login_required
from jobber.forms import *
import PyPDF2
from tika import parser
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

@app.route("/")
@app.route("/home")
@login_required()
def home():
    page_num=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(per_page=2,page=page_num)
    print(posts.items[1].likers)
    return render_template('home.html',posts=posts,len=len)

@app.route("/employee/searchjobs",methods=['GET', 'POST'])
@login_required(role='employee')
def searchjobs():
    page_num=request.args.get('page',1,type=int)
    if(request.method=='POST'):
        jobs=Job.query
        if(request.form['title']!=""):
            jobs=jobs.filter(Job.title.contains(request.form['title']))
        if(request.form['location']!=""):
            jobs=jobs.filter(Job.location.contains(request.form['location']))
        if(request.form['typeofjob']!=""):
            jobs=jobs.filter(Job.typeofjob.contains(request.form['typeofjob']))
    else:
        jobs=Job.query
    jobs=jobs.order_by(Job.date_posted.desc()).paginate(per_page=10,page=page_num)
    return render_template('searchjobs.html',title='Search for jobs',jobs=jobs)

@app.route("/employee/appliedjobs",methods=['GET', 'POST'])
@login_required(role='employee')
def appliedjobs():
    #page_num=request.args.get('page',1,type=int)
    jobs=current_user.jobs_applied
    print(jobs)
    #jobs=jobs.order_by(Job.date_posted.desc()).paginate(per_page=10,page=page_num)
    return render_template('appliedjobs.html',title='Search for jobs',jobs=jobs)


@app.route("/employer/searchcandidates",methods=['GET', 'POST'])
@login_required(role='employer')
def searchcandidates():
    users=[]
    if(request.method=='POST'):
        keywords=request.form['keywords']
        keywords=keywords.split()
        for keyword in keywords:
            key=Keyword.query.get(keyword)
            if(key):
                users.extend(key.users)
    users=(list(dict.fromkeys(users)))
    return render_template('searchcandidates.html',title='Search for candidates',users=users)



@app.route("/employee/viewjobinfo",methods=['GET', 'POST'])
@login_required(role='employee')
def viewjobinfo():
    job_id=request.args.get('job_id',0,type=int)
    job=Job.query.get(job_id)
    h=db.session.query(jobs_applied_table).filter_by(user_id=current_user.id).filter_by(job_id=job_id).first()
    if(not h):
        flag=0
    else:
        flag=h[2]
    if(request.method=='POST'):
        #current_user.jobs_applied.append(job)
        statement = jobs_applied_table.insert().values(job_id=job_id, user_id=current_user.id,selected=0)
        db.session.execute(statement)
        db.session.commit()
        flash(f'Applied for job')
    return render_template('viewjobinfo.html',title=job.title,job=job,selected=flag)

@app.route("/employee/chooseinterviewtimeslot",methods=['GET', 'POST'])
@login_required(role='employee')
def chooseinterviewtimeslot():
    job_id=request.args.get('job_id',0,type=int)
    job=Job.query.get(job_id)
    if(request.method=='POST'):
        interview_id = request.form['interview_id']
        interview=Interview.query.get(interview_id)
        flag=0
        for inter in current_user.interviews:
            if(job_id==inter.job):
                current_user.interviews.remove(inter)
                db.session.commit()
                if(int(inter.id)!=int(interview_id)):
                    current_user.interviews.append(interview)
                    db.session.commit()
                flag=1
                break
        if(flag==0):
            current_user.interviews.append(interview)
            db.session.commit()
        flash("Selected Interview")
    return render_template('chooseinterviewtimeslot.html',title=job.title,interviews=job.interviews)

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

@app.route("/employer/applicants",methods=['GET', 'POST'])
@login_required(role='employer')
def checkapplicants():
    job_id=request.args.get('job_id',1,type=int)
    job=Job.query.get(job_id)
    return render_template('checkapplicants.html',title='job.title',job=job)

@app.route("/employer/applicant",methods=['GET', 'POST'])
@login_required(role='employer')
def viewapplicant():
    user_id=request.args.get('user_id',0,type=int)
    job_id=request.args.get('job_id',0,type=int)
    h=db.session.query(jobs_applied_table).filter_by(user_id=user_id).filter_by(job_id=job_id).first()
    flag=h[2]
    user=User.query.get(user_id)
    if(request.method=='POST'):
        u=User.query.get(user_id)
        j=Job.query.get(job_id)
        u.jobs_applied.remove(j)
        db.session.commit()
        if(h[2]==0):
            statement = jobs_applied_table.insert().values(job_id=job_id, user_id=user_id,selected=1)
            flag=1
        else:
            statement = jobs_applied_table.insert().values(job_id=job_id, user_id=user_id,selected=0)
            flag=0
        db.session.execute(statement)
        db.session.commit()
        if(flag==1):
            flash(f'Candidate Selected')
        else:
            flash(f'Candidate DeSelected')
    return render_template('viewapplicant.html',title='user.name',user=user,selected=flag)

@app.route("/employer/jobs",methods=['GET', 'POST'])
@login_required(role='employer')
def viewjob():
    if(request.method=='POST'):
        job_id = request.form['job_id']
        job=Job.query.get(job_id)
        for i in job.interviews:
            db.session.delete(i)
        db.session.delete(job)
        db.session.commit()
        flash(f'Deleted job')
    return render_template('viewJobs.html',title='View Jobs',jobs=current_user.jobs,user=current_user.company_name)

@app.route("/employer/interviews/<job_id>")
@login_required(role='employer')
def viewinterviews(job_id):
    job=Job.query.get(job_id)
    interviews=job.interviews
    return render_template('viewinterviews.html',title='View Interviews for '+str(job.title),job_title=job.title,interviews=interviews)

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
    return render_template('setInterview.html',title='Set Interview Form',form=form,job_id=Job.query.get(job_id).title)


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
                    cv_fn=save_cv(form.cv.data,current_user)
                    current_user.cv=cv_fn
                    if(not current_user.post):
                        post = Post(title=current_user.name, content=form.content.data, author=current_user)
                        db.session.add(post)
                        db.session.commit()
                        post.old_cv=cv_fn
                    else:
                        current_user.post.old_cv=cv_fn                        
                        current_user.post.content=form.content.data
                        current_user.post.date_posted=datetime.utcnow()
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

def save_cv(cv,current_user):
    _,f_ext=os.path.splitext(cv.filename)
    cv_fn=current_user.email+str(int(round(time.time() * 1000)))+f_ext
    cv_path=os.path.join(app.root_path,'static/cvs',cv_fn)
    cv.save(cv_path)
    keywords=get_keywords(cv_path)
    current_user.keywords=[]
    print(keywords)
    for keyword in keywords:
        k=Keyword.query.get(str(keyword))
        if(not k):
            k=Keyword(title=str(keyword))
            db.session.add(k)
            db.session.commit()
        current_user.keywords.append(k)
    db.session.commit()
    #current_user.keywords.append()
    return cv_fn


@app.route("/employee/account/<emp_id>", methods=['GET', 'POST'])
@login_required()
def employeeaccount(emp_id):
    employee=User.query.filter_by(id=emp_id).filter_by(type='employee').first_or_404()
    return render_template('employeeAccount.html',title='Employee Account',employee=employee)

@app.route("/employer/account/<emp_id>", methods=['GET', 'POST'])
@login_required()
def employeraccount(emp_id):
    employer=User.query.filter_by(id=emp_id).filter_by(type='employer').first_or_404()
    return render_template('employerAccount.html',title='Employer Account',employer=employer)


@app.route("/employee/account/update", methods=['GET', 'POST'])
@login_required(role='employee')
def employeeaccountupdate():
    form=EmployeeUpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn=save_picture(form.picture.data)
            current_user.profile_picture=picture_fn
            db.session.commit()
        if not (current_user.email==form.email.data.lower()):
            current_user.email=form.email.data.lower()
        if form.cv.data:
            cv_fn=save_cv(form.cv.data,current_user)
            current_user.cv=cv_fn
            if(not current_user.post):
                post = Post(title=current_user.name, content=form.content.data, author=current_user)
                db.session.add(post)
                db.session.commit()
                post.old_cv=cv_fn
            else:
                current_user.post.old_cv=cv_fn
                current_user.post.content=form.content.data
                current_user.post.date_posted=datetime.utcnow()
        current_user.name=form.name.data
        db.session.commit()
        flash(f'Account Updated')
        return redirect(url_for('employeeaccount',emp_id=current_user.id))
    elif request.method=='GET':
        form.email.data=current_user.email
        form.name.data=current_user.name
        form.content.data="Uploaded CV"
    return render_template('employeeAccountUpdate.html',title='Employee Account',form=form)

@app.route("/employer/account/update", methods=['GET', 'POST'])
@login_required(role='employer')
def employeraccountupdate():
    form=EmployerUpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn=save_picture(form.picture.data)
            current_user.profile_picture=picture_fn
        if not (current_user.email==form.email.data.lower()):
            current_user.email=form.email.data.lower()
        current_user.name=form.name.data
        current_user.company_name=form.company_name.data
        current_user.company_gst_number=form.company_gst_number.data
        current_user.company_info=form.company_info.data
        current_user.position=form.position.data
        db.session.commit()
        flash(f'Account Updated')
        return redirect(url_for('employeraccount',emp_id=current_user.id))
    elif request.method=='GET':
        form.email.data=current_user.email
        form.name.data=current_user.name
        form.company_name.data=current_user.company_name
        form.company_gst_number.data=current_user.company_gst_number
        form.company_info.data=current_user.company_info
        form.position.data=current_user.position
    return render_template('employerAccountUpdate.html',title='Employer Account',form=form)

@app.route("/employer/like_post", methods=['POST','GET'])
def like_post():
    json=request.get_json()
    post=Post.query.get(json['post_id'])
    if(post in current_user.liked_posts):
        current_user.liked_posts.remove(post)
    else:
        current_user.liked_posts.append(post)
    db.session.commit()
    return jsonify({"message":"Done"}),200

def get_keywords(filename):
    #open allows you to read the file
    pdfFileObj = open(filename,'rb')
    #The pdfReader variable is a readable object that will be parsed
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #discerning the number of pages will allow us to parse through all #the pages
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    #The while loop will read each page
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
    #This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
    if text != "":
        text = text
    #If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
    else:
        raw = parser.from_file(filename)
        text =raw['content'] 
    # Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
    # Now, we will clean our text variable, and return it as a list of keywords.
    #The word_tokenize() function will break our text phrases into #individual words
    tokens = word_tokenize(text)
    #we'll create a new list which contains punctuation we wish to clean
    punctuations = ['(',')',';',':','[',']',',','-']
    #We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
    stop_words = stopwords.words('english')
    #We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
    keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
    keywords=(list(dict.fromkeys(keywords)))
    keywords=list(map(lambda x:x.lower(),keywords))
    return(keywords)