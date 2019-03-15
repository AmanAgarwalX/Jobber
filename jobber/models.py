from jobber import db,login_manager
from flask_login import UserMixin,current_user
from functools import wraps

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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

    def get_urole(self):
            return self.type
    def __repr__(self):
        if(self.type=='employee'):
            return f"User('{self.id}','{self.type}','{self.name}','{self.email}')"
        else:
            return f"User('{self.name}','{self.email}','{self.profile_picture}','{self.company_name}','{self.company_info}','{self.position}')"



        