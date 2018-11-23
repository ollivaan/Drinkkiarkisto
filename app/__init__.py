# coding=utf-8
from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
# Kaytetään tasks.db-nimista SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
import os

if os.environ.get("HEROKU"):
    #os.environ['DATABASE_URL'] = 'postgres://hnaggozxuiysls:b01b96833a5d96e5aa0d8784c6de2797ca97aa8e27cb496ebcfe99cd35c45c5c@ec2-54-235-193-0.compute-1.amazonaws.com:5432/db9hatdvafk754'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///drinks.db"    
    app.config["SQLALCHEMY_ECHO"] = True

# Pyydetään sqlalchemyä tulostamaan kaikki sql-kyselyt
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

from app.drinkIngredients import models
from app.ingredientUser import models
from app.drinkUser import models


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
    
try: 
    db.create_all()
except:
    pass