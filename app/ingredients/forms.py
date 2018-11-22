from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class IngredientForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=2, max=50)])
    done = BooleanField("If you have this ingredient then mark this box")

    class Meta:
        csrf = False
class IngredientEditForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=2, max=50)])
    done = BooleanField("If you have this ingredient then mark this box")

    class Meta:
        csrf = False        