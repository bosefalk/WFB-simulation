from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class UnitForm(FlaskForm):
    name1 = StringField('name', validators = [DataRequired()])
    S1 = IntegerField('S', validators = [DataRequired()])
    name2 = StringField('name', validators = [DataRequired()])
    S2 = IntegerField('S', validators = [DataRequired()])
