from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class DrinkForm(FlaskForm):
    name = StringField("Drink name", [validators.Length(min=2, max=50)])
    done = BooleanField("If you have tested then mark this box")

    class Meta:
        csrf = False