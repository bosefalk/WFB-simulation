from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class UnitForm(Form):
    name = StringField('name')
    S = IntegerField('S')
