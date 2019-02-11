from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from Jim.models import User


# Creating form that will be used on sign up page, validators create set rules e.g. Password must be longer than
# 6 characters
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=60)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Sign Up')

    # Function that checks if username has already been taken
    def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken, please chose a different one')

    # Function that checks if email has already been taken
    def validate_email(self, email):
            email = User.query.filter_by(username=email.data).first()
            if email:
                raise ValidationError('That email is taken, please chose a different one')


# Creating form which will be used to login
class LoginForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# Creating class that will allow users to change their account information
class UpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed('jpg', 'png', 'gif')])
    submit = SubmitField('Update Account Information')

    # Creating function that will check whether new username is already taken
    def validate_username(self, username):
        if username.data != current_user.data:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is already taken, please chose a different one.')

    # Creating function that will check whether new email has been taken
    def validate_email(self, email):
        if email.data != current_user.data:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError("This email is already taken, please chose another one.")
