from app import app, db
from flask import redirect, render_template, request, url_for
from app.drinks.models import Drink
from app.drinks.forms import DrinkForm

@app.route("/drinks", methods=["GET"])
def drinks_index():
    return render_template("drinks/list.html", drinks = Drink.query.all())

@app.route("/drinks/new/")
def drinks_form():
    return render_template("drinks/new.html", form = DrinkForm())

@app.route("/drinks/<drink_id>/", methods=["POST"])
def drinks_set_done(drink_id):
    d = Drink.query.get(drink_id)
    d.done = True
    db.session().commit()
    return redirect(url_for("drinks_index"))

@app.route("/drinks/", methods=["POST"])
def drinks_create():
    form = DrinkForm(request.form)
    if not form.validate():
        return render_template("drinks/new.html", form = form)
    d = Drink(form.name.data)
    d.done = form.done.data

    db.session().add(d)
    db.session().commit()
    
    return redirect(url_for("drinks_index"))

