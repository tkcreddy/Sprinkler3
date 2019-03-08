from flask_wtf import FlaskForm,Form
from wtforms import StringField,IntegerField, SubmitField,HiddenField,FieldList,FormField

from wtforms import validators, ValidationError


class ZoneForm(FlaskForm):
    id = HiddenField("id")
    name = StringField("name")
    submit = SubmitField("Save")


class ZonelistForm(FlaskForm):
    zonelistname = StringField("name")
    zonedetails = FieldList(FormField(ZoneForm))
