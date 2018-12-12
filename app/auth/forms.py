from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField

class LoginForm(FlaskForm):
    username = StringField("Username", render_kw={"placeholder": "Username"})
    password = PasswordField("Password", render_kw={"placeholder": "Password"})

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Give name", [validators.Length(min=3, max=20)], render_kw={"placeholder": "Nimi"})
    username = StringField("Give username", [validators.Length(min=3, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField("Password", [validators.Length(min=3, max=20)], render_kw={"placeholder": "Password"})

    class Meta:
        csrf = False

