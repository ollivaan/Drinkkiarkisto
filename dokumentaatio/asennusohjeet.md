
# Asennusohjeet:

Asenna aluksi [python 3.6](https://www.python.org/downloads/release/python-360/)  ja [PIP-paketinhallinta järjestelmän](https://pip.pypa.io/en/stable/reference/pip_download/), jos sinulla ei ole niitä.

# Paikalliseen ympäristöön

git clone git@github.com:ollivaan/Drinkkiarkisto.git
cd Drinkkiarkisto
python3 -m venv venv
python3 run.py

Tämän jälkeen sovellus aukeaa lokaalisti portissa: 5000
eli oma ip:5000


# Heroku
Luo tunnukset [herokuun](https://www.heroku.com/) ja asenna [heroku cli](https://devcenter.heroku.com/articles/heroku-cli) 
heroku create drinkkiarkisto
heroku config:set HEROKU=1
heroku addons:add heroku-postgresql-dev
git remote add heroku <sinun osoite>/drinkkiarkisto.git
git add -A
git commit -m "Initial commit"
git push heroku master



 

