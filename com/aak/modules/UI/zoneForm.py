from flask_wtf import FlaskForm,Form
from wtforms import StringField,TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField,HiddenField

from wtforms import validators, ValidationError


class ZoneForm(FlaskForm):
    id = HiddenField("id")
    name =StringField("name")
    submit = SubmitField("Save")