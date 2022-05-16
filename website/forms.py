from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash

class LoginForm(FlaskForm):
   username = StringField('Username:', validators=[InputRequired(), Length(min=5, max=20)])
   password = PasswordField('Password:', validators=[InputRequired(), Length(min=8, max=80)])