from app import db
from app.drinkIngredients import models
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    #children = relationship("Child", secondary=association_table, backref="parents")
    name = db.Column(db.String(144), nullable=False)
    iHaveIt = db.Column(db.Boolean, nullable=False)

#    drinks = db.relationship("Drink", secondary=IngredientsInDrink, backref="Drinks")

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
             
    def __init__(self, name):
        self.name = name
        self.iHaveIt = False    