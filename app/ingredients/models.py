from app import db
from app.models import Base





class Ingredient(Base):
    _tablename_ ="ingredient"




    name = db.Column(db.String(144), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    drink = db.relationship('DrinkIngredient', back_populates='ingredient')
    user = db.relationship("User", back_populates="ingredients")
    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return '<Ingredient %r>' % (self.name)             



#         drinkit = Drink.query.all()

#         palautusarvo = []
#         for drink in drinkit:
#             liitos = DrinkIngredient.drink_id
# #            aineksetLiitosTaulusta = DrinkIngredient.ingredient_id
#             ingredients = Ingredient.query.get_or_404(DrinkIngredient.ingredient_id)
# #            ingredients = Ingredient.getbyid(liitos.ingredient_id)
            
#             palautusarvo.append({drink: drink, ingredients: ingredients})

#         return palautusarvo
