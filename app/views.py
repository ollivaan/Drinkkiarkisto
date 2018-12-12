from flask import render_template
from app import app
from app.auth.models import User

@app.route("/")
def index():
  return render_template("index.html")
  #, need_to_create = User.find_users_with_no_drinks()
  #base poistettu , bravo_these_users = User.find_users_with_five_drinks()
  # , need_to_drink = User.find_users_with_no_drinks(), need_to_slow_down = User.find_users_with_five_drinks()

