from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    number1 = IntegerField('number1', validators=[DataRequired()])
    number2 = IntegerField('number2', validators=[DataRequired()])
    
    
class PropertyForm(FlaskForm):
    address = StringField('address', validators=[DataRequired()])
    start_date = DateField('start_date', validators=[DataRequired()])
    duration = IntegerField('duration', validators=[DataRequired()])
    rent = IntegerField('rent', validators=[DataRequired()])