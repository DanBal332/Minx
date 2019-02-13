from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Jim.models import User


# Class that will serve as form registration of user
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Function that will check whether username has been taken (registration)
    def validate_username(self, username):
        user = User.query.filber_by(username=username.data).first()
        if user:
            raise ValidationError("This username has been taken, please chose a different username.")

    # Function that will check whether email has been taken (login)
    def validate_email(self, email):
        email = User.query.filber_by(email=email.data).first()
        if email:
            raise ValidationError("This email has been taken, please chose a different email.")


# Class that will serve as form login of user
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
