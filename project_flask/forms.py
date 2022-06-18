from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class Registrationform(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    confirm_password = PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    sumbit = SubmitField(label='Sign Up',validators=[DataRequired()])


class Loginform(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired()])
    password = PasswordField(label='Password',validators=[DataRequired()])
    sumbit = SubmitField(label='Login',validators=[DataRequired()])

class ResetRequestform(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired()])
    sumbit = SubmitField(label='Reset Password',validators=[DataRequired()])


class ResetPasswordform(FlaskForm):
    password = PasswordField(label='Password',validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    sumbit = SubmitField(label='Change Password',validators=[DataRequired()])
