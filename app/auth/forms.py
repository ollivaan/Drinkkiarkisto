from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Give name")
    username = StringField("Give username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

