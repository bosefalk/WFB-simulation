from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class UnitForm(FlaskForm):
    name1 = StringField('name1', validators = [DataRequired()])
    models1 = IntegerField('models1', validators = [DataRequired()])
    WS1 = IntegerField('WS1', validators = [DataRequired()])
    S1 = IntegerField('S1', validators = [DataRequired()])
    T1 = IntegerField('T1', validators = [DataRequired()])
    I1 = IntegerField('I1', validators = [DataRequired()])
    Sv1 = IntegerField('Sv1', validators = [DataRequired()])
    Ld1 = IntegerField('Ld1', validators = [DataRequired()])
    name2 = StringField('name2', validators=[DataRequired()])
    models2 = IntegerField('models2', validators=[DataRequired()])
    WS2 = IntegerField('WS2', validators=[DataRequired()])
    S2 = IntegerField('S2', validators=[DataRequired()])
    T2 = IntegerField('T2', validators=[DataRequired()])
    I2 = IntegerField('I2', validators=[DataRequired()])
    Sv2 = IntegerField('Sv2', validators=[DataRequired()])
    Ld2 = IntegerField('Ld2', validators=[DataRequired()])

    runs = IntegerField('runs', validators=[DataRequired()])

