from app import db
from app.models import Base
from app.ingredients.models import Ingredient
from app.auth.models import User
from sqlalchemy.sql import text


class Drink(Base):
    __tablename__ = "drink"

 
    ingredients = db.relationship('DrinkIngredient', back_populates='drink')
    
    name = db.Column(db.String(50), nullable=False)


    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    user = db.relationship("User", back_populates="drinks")

    def __init__(self, name):
        self.name = name
        self.accepted = False

    # def haelista():
    #     stmt = text("SELECT Drink.id, Drink.name, Drink.date_created, Ingredient.name AS ingredientname FROM Drink"
    #                 " LEFT JOIN drink_ingredient ON drink_ingredient.drink_id = Drink.id"
    #                 " LEFT JOIN Ingredient ON Ingredient.id = drink_ingredient.ingredient_id"
    #                 " GROUP BY Drink.id, Ingredient.id")
    #     res = db.engine.execute(stmt)


    #     return res    

class DrinkIngredient(Base):
    __tablename__ = 'drink_ingredient'
    id = db.Column(db.Integer, primary_key=True)

    drink_id = db.Column(db.Integer, db.ForeignKey(Drink.id))
    ingredient_id = db.Column(db.Integer, db.ForeignKey(Ingredient.id))

    drink = db.relationship('Drink', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='drink')
