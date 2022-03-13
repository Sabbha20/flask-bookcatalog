from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.auth.models import User


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email already exists')


class RegistrationForm(FlaskForm):
    name = StringField('Enter Name: ', validators=[DataRequired(), Length(3, 15, message='betwwen 3 & 15 characters')])
    email = EmailField('Enter Email: ', validators=[DataRequired(), email_exists])
    password = PasswordField('Enter Password: ',
                             validators=[DataRequired(), Length(5, message='minimum 5 characters of password'),
                                         EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    password=PasswordField('Password: ', validators=[DataRequired()])
    stay_logged_in=BooleanField('stay logged in')
    submit=SubmitField('Login')