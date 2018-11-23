from app import db

class ingredientUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('Ingredient.id'), nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
