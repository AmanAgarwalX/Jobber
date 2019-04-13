from jobber import db,login_manager
from flask_login import UserMixin,current_user
from functools import wraps
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


likes_table = db.Table('likes', db.Column('user_id',db.Integer, db.ForeignKey('user.id')),db.Column('post_id', db.Integer, db.ForeignKey('post.id')))
jobs_applied_table = db.Table('jobs_applied', db.Column('user_id',db.Integer, db.ForeignKey('user.id')),db.Column('job_id', db.Integer, db.ForeignKey('job.id')),db.Column('selected', db.Integer))
interviews_table = db.Table('interviews', db.Column('user_id',db.Integer, db.ForeignKey('user.id')),db.Column('interview_id', db.Integer, db.ForeignKey('interview.id')))
keyword_table=db.Table('keywords', db.Column('user_id',db.Integer, db.ForeignKey('user.id')),db.Column('keyword_title', db.Integer, db.ForeignKey('keyword.title')))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.String(10),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    name=db.Column(db.String(120),nullable=False)
    profile_picture=db.Column(db.String(50),nullable=False,default='default.jpg')
    password=db.Column(db.String(12),nullable=False)
    company_name=db.Column(db.String(120),nullable=True)
    company_gst_number=db.Column(db.String(120),nullable=True)
    company_info=db.Column(db.Text,nullable=True)
    position=db.Column(db.String(120),nullable=True)
    cv=db.Column(db.String(50),default='none.pdf')
    post = db.relationship('Post', backref='author', lazy=True,uselist=False)
    jobs = db.relationship('Job', backref='author', lazy=True)
    liked_posts = db.relationship('Post', secondary=likes_table, backref=db.backref('likers', lazy=True))
    keywords = db.relationship('Keyword', secondary=keyword_table, backref=db.backref('users', lazy=True))
    interviews = db.relationship('Interview', secondary=interviews_table, backref=db.backref('employees', lazy=True))
    jobs_applied = db.relationship('Job', secondary=jobs_applied_table, backref=db.backref('employees', lazy=True))

    def get_urole(self):
            return self.type
    def __repr__(self):
        if(self.type=='employee'):
            return f"User('{self.id}','{self.type}','{self.name}','{self.email}')"
        else:
            return f"User('{self.name}','{self.email}','{self.profile_picture}','{self.company_name}','{self.company_info}','{self.position}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    old_cv=db.Column(db.String(50))    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Keyword(db.Model):
    title = db.Column(db.String(100), primary_key=True)
    def __repr__(self):
        return f"Keywords('{self.title}')"

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    typeofjob = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    interviews = db.relationship('Interview', backref='job_ref', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Job('{self.title}', '{self.date_posted}')"


class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    job = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

    def __repr__(self):
        return f"Interview('{self.title}')"