
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class AddressForm(Form): 
      city = StringField('City')
      procedure = StringField('Procedure',validators =[DataRequired("Please enter your Procedure or City")])
      submit = SubmitField('Go')
