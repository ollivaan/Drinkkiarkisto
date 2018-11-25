from app import db
from sqlalchemy.sql import text
class User(db.Model):
    __tablename__="account"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp()),
    onupdate=db.func.current_timestamp()

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    drinks = db.relationship("Drink", backref='account', lazy=True)
    ingredients = db.relationship("Ingredient", backref='account', lazy=True)
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

"""     @staticmethod
    def find_users_with_no_drinks():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Drink ON Drink.account_id = Account.id"
                     " WHERE (Drink.done IS null OR Drink.done = 1)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Drink.id) = 0")
                      
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
    @staticmethod
    def find_users_with_ten_drinks():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Drink ON Drink.account_id = Account.id"
                    " WHERE (Drink.done >= 10)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Drink.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response    """                 