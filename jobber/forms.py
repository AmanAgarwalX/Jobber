from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,ValidationError
from wtforms.validators import DataRequired,Email,Length,EqualTo
from jobber.models import User
from flask_login import current_user

class EmployeeRegistrationForm(FlaskForm):
    email=StringField('Email Address',validators=[DataRequired(),Email()])
    name=StringField('Name',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=12)])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data.lower()).first()
        if(user):
            raise ValidationError('That email is already registered')

class EmployeeLoginForm(FlaskForm):
    email=StringField('Email Address',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

class EmployerRegistrationForm(FlaskForm):
    email=StringField('Email Address',validators=[DataRequired(),Email()])
    name=StringField('Name',validators=[DataRequired()])
    company_name=StringField('Company Name',validators=[DataRequired()])
    company_gst_number=StringField('Company GST Number',validators=[DataRequired()])
    company_info=TextAreaField('Company Info',validators=[DataRequired()])
    position=StringField('Position in company',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=12)])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data.lower()).first()
        if(user):
            raise ValidationError('That email is already registered')

class EmployerLoginForm(FlaskForm):
    email=StringField('Email Address',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

class EmployeeUpdateAccountForm(FlaskForm):
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpeg','png','JPG'])])
    email=StringField('Email Address',validators=[DataRequired(),Email()])
    name=StringField('Name',validators=[DataRequired()])
    submit=SubmitField('Update')
    def validate_email(self,email):
        if(email.data.lower() != current_user.email):    
            user=User.query.filter_by(email=email.data.lower()).first()
            if(user):
                raise ValidationError('That email is already registered')

class EmployerUpdateAccountForm(FlaskForm):
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpeg','png','JPG'])])
    email=StringField('Email Address',validators=[DataRequired(),Email()])
    name=StringField('Name',validators=[DataRequired()])
    company_name=StringField('Company Name',validators=[DataRequired()])
    company_gst_number=StringField('Company GST Number',validators=[DataRequired()])
    company_info=TextAreaField('Company Info',validators=[DataRequired()])
    position=StringField('Position in company',validators=[DataRequired()])
    submit=SubmitField('Update')
    def validate_email(self,email):
        if(email.data.lower() != current_user.email):    
            user=User.query.filter_by(email=email.data.lower()).first()
            if(user):
                raise ValidationError('That email is already registered')
