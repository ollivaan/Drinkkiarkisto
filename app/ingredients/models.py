from app import db


#from app.drinks import models
#from app.ingredients import models 
#IngredientsInDrink = db.Table('IngredientsInDrink',
#    db.Column('ingredient_id', db.Integer, db.ForeignKey('Ingredient.id'), primary_key=True),
#    db.Column('drink_id', db.Integer, db.ForeignKey('Drink.id'), primary_key=True))

class drinkIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drink_id = db.Column(db.Integer, db.ForeignKey("drink.id"), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), primary_key=True)
    ingredient = db.relationship("Ingredient")



class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    #children = relationship("Child", secondary=association_table, backref="parents")
    name = db.Column(db.String(144), nullable=False)
    iHaveIt = db.Column(db.Boolean, nullable=False)
    drinks = db.relationship("Drink", secondary=drinkIngredient.__table__, lazy="select", viewonly=True)
#    drinks = db.relationship("Drink", secondary=IngredientsInDrink, backref="Drinks")
    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'))
#    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
             
    def __init__(self, name):
        self.name = name
        self.iHaveIt = False    