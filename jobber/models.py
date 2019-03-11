from jobber import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

class Employee(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True,nullable=False)
    name=db.Column(db.String(120),nullable=False)
    profile_picture=db.Column(db.String(50),nullable=False,default='default.jpg')
    password=db.Column(db.String(12),nullable=False)
    def __repr__(self):
        return f"User('{self.name}','{self.email}','{self.profile_picture}')"