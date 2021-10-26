from wtforms import FloatField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class SumForm(FlaskForm):
    a = FloatField(validators=[DataRequired()], default=0)
    b = FloatField(validators=[DataRequired()], default=0)
