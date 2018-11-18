# coding=utf-8
from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
# Kaytetään tasks.db-nimista SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///drinks.db"
# Pyydetään sqlalchemyä tulostamaan kaikki sql-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

#luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)
#Luetaan kansiosta app tiedoston views sisältö
from app import views
#luodaan lopulta tarvittavat tietokantataulut sisältö
from app.drinks import models
from app.drinks import views

from app.auth import models
from app.auth import views

from app.ingredients import models
from app.ingredients import views


# kirjautuminen
from app.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db.create_all()
