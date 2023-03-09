from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    bedroom = IntegerField('No. of Bedrooms', validators=[InputRequired()])
    bathroom = DecimalField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type=  SelectField('Property Type', choices=[("house","House"),("apartment","Apartment")], validate_choice=True)
    description = TextAreaField("Description",validators=[InputRequired()])
    photo = FileField('Photo' , validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
   