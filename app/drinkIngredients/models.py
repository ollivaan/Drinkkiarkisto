from app import db

class drinkIngredient(db.Model):
    drink_id = db.Column(db.Integer, db.ForeignKey('drink_id'),
    nullable=False, primary_key = True)
#    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), 
#    nullable=False)
    ingredient_id =db.Column(db.Integer, db.ForeignKey('ingredient_id'), nullable=False, primary_key = True)
