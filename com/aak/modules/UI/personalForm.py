from flask_wtf import FlaskForm,Form
from wtforms import StringField,TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError


class PersonalForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired("Please enteryour name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                validators.Email("Please enter your email address.")])
    zip = IntegerField("Zip", [validators.DataRequired("Please enter Zip Code."), validators.length(max=6)])
    country = StringField('Country', [validators.DataRequired("Please enter Country Code."),
                                validators.length(max=2)])
    owm_appid = StringField("owm_appid")
    submit = SubmitField("Save")