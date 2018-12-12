from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class IngredientForm(FlaskForm):
    name = StringField("Ainesosan nimi", [validators.Length(min=2, max=50)], render_kw={"placeholder": "Nimi"})
#    done = BooleanField("If you have this ingredient then mark this box")

    class Meta:
        csrf = False
        
class IngredientEditForm(FlaskForm):
    name = StringField("Ainesosan nimi", [validators.Length(min=2, max=50)], render_kw={"placeholder": "Nimi"})
#    done = BooleanField("If you have this ingredient then mark this box")

    class Meta:
        csrf = False        