from app import db

class drinkUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #drink_id = db.Column('Drink.id', db.Integer, db.ForeignKey('Drink.id'), nullable=False)
    #user_id =db.Column('account_id', db.Integer, db.ForeignKey('account.id'), nullable=False)

