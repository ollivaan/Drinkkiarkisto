from app import db

from sqlalchemy.sql import text



class DrinkIngredient(db.Model):
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    drink_id = db.Column(db.Integer, db.ForeignKey('drink.id'), primary_key=True)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


    name = db.Column(db.String(144), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return '<Ingredient %r>' % (self.name)             

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    recipe = db.relationship("DrinkIngredient", backref="Drink")
    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'))


    def __init__(self, name):
        self.name = name
    
    def haelista():
        stmt = text("SELECT Drink.id, Drink.name, Drink.date_created, Ingredient.name AS ingredientname FROM Drink"
                    " LEFT JOIN drink_ingredient ON drink_ingredient.drink_id = Drink.id"
                    " LEFT JOIN Ingredient ON Ingredient.id = drink_ingredient.ingredient_id"
                    " GROUP BY Drink.id, Ingredient.id")
        res = db.engine.execute(stmt)


        return res
    
    # def haelista():
    #     drinkit = getall()

    #     palautusarvo = []
    #     for drink in drinks:
    #         liitos = haeliitostaulu(drink.id)
    #         ingredients = Ingredient.getbyid(liitos.ingredient_id)

    #         palautusarvo.append({drinkki: drink, ingredients: ingredients})

    #     return palautusarvo
#     def haelista2():
#         drinkit = Drink.query.all()

#         palautusarvo = []
#         for drink in drinkit:
#             liitos = DrinkIngredient.drink_id
# #            aineksetLiitosTaulusta = DrinkIngredient.ingredient_id
#             ingredients = Ingredient.query.get_or_404(DrinkIngredient.ingredient_id)
# #            ingredients = Ingredient.getbyid(liitos.ingredient_id)
            
#             palautusarvo.append({drink: drink, ingredients: ingredients})

#         return palautusarvo