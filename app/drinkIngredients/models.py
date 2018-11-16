from app import db

class drinkIngredient(db.Model):
    drink_id = db.Column(db.Integer)
    ingredient_id =db.Column(db.Integer) 