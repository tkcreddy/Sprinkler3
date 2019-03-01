from flask_wtf import Form
from wtforms import StringField,TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError


class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired("Please enteryour name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                validators.Email("Please enter your email address.")])
    Zip = IntegerField("zip", [validators.DataRequired("Please enter Zip Code."), validators.length(max=2)])
    Country = StringField('Country', [validators.DataRequired("Please enter Country Code."),
                                validators.length(max=2)])
    owm_appid = TextAreaField("owm_appid")
    submit = SubmitField("Send")