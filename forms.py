from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
SQLALCHEMY_TRACK_MODIFICATIONS = False

class SignupForm(FlaskForm):
  first_name = StringField('First name', validators=[DataRequired('Please enter your first name')])
  last_name = StringField('Last name', validators=[DataRequired('Please enter your last name')])
  email = StringField('Email', validators=[DataRequired('Please enter your email'), Email('Please enter your email')])
  password = PasswordField('Password', validators=[DataRequired('Please enter your password'), Length(6, 10, 'Your password must be at least 6 chars long.')])
  submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired('Please enter your email address'), Email('Please enter your email address.')])
  password = PasswordField('Password', validators=[DataRequired('Please enter your password')])
  submit = SubmitField('Sign in')
  
  