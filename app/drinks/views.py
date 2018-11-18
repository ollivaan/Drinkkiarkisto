from app import app, db
from flask import redirect, render_template, request, url_for
from app.drinks.models import Drink
from app.drinks.forms import DrinkForm
from flask_login import login_required, current_user

@app.route("/drinks", methods=["GET"])
def drinks_index():
    return render_template("drinks/list.html", drinks = Drink.query.all())

@app.route("/drinks", methods=["GET","POST"])
def drinks_delete(drink_id):
    d = Drink.query.get_or_404(drink_id)
    db.session().delete(d)
    db.session.commit()
    
    return redirect(url_for("drinks_index"))


@app.route("/drinks/new/")
@login_required
def drinks_form():
    return render_template("drinks/new.html", form = DrinkForm())

@app.route("/drinks/drink/<int:drink_id>", methods=["GET"])
@login_required
def onedrink(drink_id):
    drink = Drink.query.get_or_404(drink_id)
    return render_template("drinks/drink.html", name=drink.name, drink=drink)

@app.route("/drinks/<drink_id>/", methods=["POST"])
@login_required
def drinks_set_done(drink_id):
    d = Drink.query.get(drink_id)
    d.done = True
    #d.account_id = current_user.id
    db.session().commit()
    return redirect(url_for("drinks_index"))

@app.route("/drinks/", methods=["POST"])
@login_required
def drinks_create():
    form = DrinkForm(request.form)
    if not form.validate():
        return render_template("drinks/new.html", form = form)
    d = Drink(form.name.data)
    d.done = form.done.data
    d.account_id = current_user.id
    db.session().add(d)
    db.session().commit()
    
    return redirect(url_for("drinks_index"))

