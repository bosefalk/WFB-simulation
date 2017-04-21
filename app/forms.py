from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class UnitForm(FlaskForm):
    name = StringField('name')
    S = IntegerField('S')
