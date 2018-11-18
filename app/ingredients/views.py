from app import app, db
from flask import redirect, render_template, request, url_for
from app.ingredients.models import Ingredient
from app.ingredients.forms import IngredientForm
from flask_login import login_required

@app.route("/ingredients", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients = Ingredient.query.all())

@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    return render_template("ingredients/new.html", form = IngredientForm())

@app.route("/ingredients/<ingredient_id>/", methods=["POST"])
@login_required
def ingredients_set_done(ingredient_id):    
    i = Ingredient.query.get(ingredient_id)
    i.iHaveIt = True
    db.session().commit()
    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/", methods=["POST"])
@login_required
def ingredients_create():
    form = IngredientForm(request.form)
    if not form.validate():
        return render_template("ingredients/new.html", form = form)
    i = Ingredient(form.name.data)
    i.done = form.done.data

    db.session().add(i)
    db.session().commit()
    
    return redirect(url_for("ingredients_index"))