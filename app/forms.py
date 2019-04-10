from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[
        ('m','Male'),('f','Female')], 
        validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email('Enter a valid email')])
    submit = SubmitField("Add Profile")