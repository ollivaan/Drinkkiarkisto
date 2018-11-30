from app import db

#IngredientsInDrink = db.Table('IngredientsInDrink',
#    db.Column('ingredient_id', db.Integer, db.ForeignKey('Ingredient.id'), primary_key=True),
#    db.Column('drink_id', db.Integer, db.ForeignKey('Drink.id'), primary_key=True))

#class drinkIngredient(db.Model):
#    id = db.Column(db.Integer, primary_key=True)

#    def __init__(self, drink_id, ingredient_id):
#        self.drink_id = drink_id
#        self.ingredient_id = ingredient_id

#drinkIngredietn.ingredient_id
#drinkIngredient.drink_id


#ingsindrink = drinkIngredient(1, 6)
#db.add(ingsindrink)
#commit