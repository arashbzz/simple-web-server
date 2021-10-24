from wtforms import FileField, IntegerField, StringField, SelectField, FloatField
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class SumForm(FlaskForm):
    a = FloatField( validators=[DataRequired()], default = 0)
    b = FloatField( validators=[DataRequired()], default = 0)

