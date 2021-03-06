from app import app, db
from flask import redirect, render_template, request, url_for, abort, flash
from app.ingredients.models import Ingredient
from app.ingredients.forms import IngredientForm, IngredientEditForm
from flask_login import login_required, current_user

@app.route("/ingredients", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients = Ingredient.query.all())

@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    return render_template("ingredients/new.html", form = IngredientForm(), legend="New ingredient")

@app.route("/ingredients/<int:ingredient_id>", methods=["POST"])
@login_required
def ingredient_delete(ingredient_id):
    i = Ingredient.query.get_or_404(ingredient_id)

    db.session().delete(i)
    db.session.commit()
    
    return redirect(url_for("ingredients_index"))


@app.route("/ingredients/<int:ingredient_id>/update", methods=["POST", "GET"])
@login_required
def ingredient_update(ingredient_id):
    i = Ingredient.query.get_or_404(ingredient_id)
    form = IngredientEditForm()

    if  request.method == 'POST':

        editform = IngredientEditForm(request.form)

        #Validoinnin tarkastus
        if not editform.validate():
            return render_template("ingredients/edit.html",
             ingredient=Ingredient.query.get_or_404(ingredient_id), form=form)


        i.name = form.name.data
        db.session.commit()


        return redirect(url_for("ingredients_index"))
    else:
        return render_template("ingredients/edit.html",
         ingredient = Ingredient.query.get_or_404(ingredient_id), form=form)


@app.route("/ingredients/<int:ingredient_id>", methods=["GET"])
@login_required
def one_ingredient(ingredient_id):
  ingredient = Ingredient.query.get_or_404(ingredient_id)
  return render_template("ingredients/ingredient.html", name=ingredient.name, ingredient=ingredient)



@app.route("/ingredients/", methods=["POST"])
@login_required
def ingredients_create():
    form = IngredientForm(request.form)
    if not form.validate():
        return render_template("ingredients/new.html", form = form)
    i = Ingredient(form.name.data)
    if current_user is not None:
        i.account_id = current_user.id
    db.session().add(i)
    db.session().commit()
    
    return redirect(url_for("ingredients_index"))