from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()], render_kw={"style": "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    bedroom = IntegerField('No. of Bedrooms', validators=[InputRequired()], render_kw={"style": "width: 300px;" "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    bathroom = DecimalField('No. of Bathrooms', validators=[InputRequired()], render_kw={"style": "width: 300px;" "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    location = StringField('Location', validators=[InputRequired()], render_kw={"style": "width: 300px;" "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    price = StringField('Price', validators=[InputRequired()], render_kw={"style": "width: 300px;" "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    type=  SelectField('Property Type', choices=[("House","House"),("Apartment","Apartment")], validate_choice=True, render_kw={"style": "width: 300px;" "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    description = TextAreaField("Description",validators=[InputRequired()], render_kw={"style": "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    photo = FileField('Photo' , validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')], render_kw={ "style": "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
   