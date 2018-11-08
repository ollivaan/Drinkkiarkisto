from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
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
db.create_all()
