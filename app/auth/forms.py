from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

