from flask_wtf.form import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
