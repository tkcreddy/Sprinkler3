from flask_wtf import FlaskForm,Form
from wtforms import StringField,TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError


class ZoneForm(FlaskForm):
    zone1 = StringField("zone1")
    zone2 = StringField("zone2")
    zone3 = StringField("zone3")
    zone4 = StringField("zone4")
    zone5 = StringField("zone5")
    zone6 = StringField("zone6")
    zone7 = StringField("zone7")
    zone8 = StringField("zone8")
    submit = SubmitField("Save")