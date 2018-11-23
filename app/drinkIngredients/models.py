from app import db

class drinkIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drink_id = db.Column(db.Integer, db.ForeignKey('Drink.id'), nullable=False)
    ingredient_id =db.Column(db.Integer, db.ForeignKey('Ingredient.id'), nullable=False)
