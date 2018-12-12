from app import app, db
from flask import redirect, render_template, request, url_for
from app.auth.models import User
from app.drinks.forms import DrinkForm, DrinkEditForm
from flask_login import login_required, current_user
from app.drinks.models import Drink, DrinkIngredient
from app.ingredients.models import Ingredient

@app.route("/drinks", methods=["GET"])
def drinks_index():
    return render_template("drinks/list.html", drinks = Drink.query.all(), lista = Drink.haelista())

@app.route("/drinks/drink/<int:drink_id>/delete", methods=["POST"])
@login_required
def drinks_delete(drink_id):

    d = Drink.query.get_or_404(drink_id)
    if d is None:
        return redirect(url_for("drinks_index"))

    db.session.delete(d)
    db.session().commit()
    return redirect(url_for("drinks_index"))

@app.route("/drinks/<int:drink_id>/update", methods=["GET", "POST"])
def drink_update(drink_id):

    return print("moi")

    # drink = Drink.query.get_or_404(drink_id)
    # form = DrinkEditForm()
    
    # if  request.method == 'POST':
    #     editform = DrinkEditForm(request.form)

    #     #Validoinnin tarkastus
    #     if not editform.validate():
    #         return render_template("drinks/edit.html",
    #          drink=Drink.query.get_or_404(drink_id), form=form)

    #     drink.name = form.name.data
    #     db.session.commit()
    #     return redirect(url_for("drinks_index", drink_id=drink.id))
    # else:
    #     return render_template("drinks/edit.html",
    #      drink = Drink.query.get_or_404(drink_id), form=form)


@app.route("/drinks/new/")
@login_required
def drinks_form():
    return render_template("drinks/new.html", form = DrinkForm())

@app.route("/drinks/drink/<int:drink_id>/attach", methods=["POST"])
def ingredient_attach_to_drink(drink_id):

    d = Drink.query.get_or_404(drink_id)

    if request.method == "POST":
        selected_ingredients = request.form.getlist("ingredients")
      
        for ingId in selected_ingredients:


            d = DrinkIngredient()
            d.drink_id = drink_id
            d.ingredient_id = ingId                
            db.session().add(d)
            db.session().commit()
                        
    return redirect(url_for("drinks_index"))

@app.route("/drinks/drink/<int:drink_id>", methods=["GET"])
@login_required
def onedrink(drink_id):
    drink = Drink.query.get_or_404(drink_id)
    return render_template("drinks/drink.html", name=drink.name, drink=drink, ingredients = Ingredient.query.all())



@app.route("/drinks/", methods=["POST"])
@login_required
def drinks_create():
    form = DrinkForm(request.form)
    if not form.validate():
        return render_template("drinks/new.html", form = form)
    d = Drink(form.name.data)
    d.account_id = current_user.id
    db.session().add(d)
    db.session().commit()
    
    return redirect(url_for("drinks_index"))
