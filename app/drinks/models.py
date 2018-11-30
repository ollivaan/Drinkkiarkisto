from app import db
from app.drinkIngredients import models

""" association_table = db.Table('association', db.Model.metadata,
    db.Column('left_id', db.Integer, db.ForeignKey('left.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('right.id'))
)

class Parent(db.Model):
    __tablename__ = 'left'
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship("Child",
                    secondary=association_table)

class Child(db.Model):
    __tablename__ = 'right'
    id = db.Column(db.Integer, primary_key=True) """

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())



    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

#    Ingredients = db.relationship("Ingredient", secondary=IngredientsInDrink)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False
	
