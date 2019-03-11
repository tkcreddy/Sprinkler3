from flask_wtf import FlaskForm,Form
from wtforms import StringField,IntegerField, SubmitField,HiddenField,FieldList,FormField

from wtforms import validators, ValidationError


class ZoneForm(FlaskForm):
    id = HiddenField("id")
    name = StringField("name")



class ZonelistForm(FlaskForm):
    zonelists = FieldList(FormField(ZoneForm))
    submit = SubmitField("Save")
