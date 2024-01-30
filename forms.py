# WTF imports
from wtforms import Form
from wtforms import StringField,TelField, IntegerField
from wtforms.validators import DataRequired, Email
from wtforms import EmailField

# Flask imports
from flask_wtf import FlaskForm

# Class
class UserForm(Form):
    nombre = StringField("nombre")
    email = EmailField("email") #crear campo de validacion correcto
    apaterno = StringField("apaterno")
    amaterno = StringField("amaterno")
    edad = IntegerField("edad")
    