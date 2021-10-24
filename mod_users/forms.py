from typing import ValuesView
from flask_wtf.form import FlaskForm
from wtforms import FileField, StringField, IntegerField, SelectField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired


class LoginForm (FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


class UserFrom(FlaskForm):
    user_name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])
    password_re = StringField(validators=[DataRequired()])
    role = SelectField(validators=[DataRequired()], choices=[(0,'applicant'), (1,'Admin')])
