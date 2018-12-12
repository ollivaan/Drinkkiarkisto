from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class DrinkForm(FlaskForm):
    name = StringField("Drinkin nimi", [validators.Length(min=2, max=50)], render_kw={"placeholder": "Drinkin nimi"})
#    done = BooleanField("If you have tested then mark this box")

    class Meta:
        csrf = False
        
class DrinkEditForm(FlaskForm):
    name = StringField("Drinkin nimi", [validators.Length(min=2, max=50)], render_kw={"placeholder": "Nimi"})
#    done = BooleanField("If you have tested then mark this box")

    class Meta:
        csrf = False        