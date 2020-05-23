from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, NumberRange
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class PlantForm(FlaskForm):
    type = StringField('Plant type', validators=[DataRequired()])
    pot = StringField('Pot type', validators=[DataRequired()])
    watering_frequency = IntegerField('Watering Frequency (days)', validators=[DataRequired(), NumberRange(min=1, max = 60)])
    submit = SubmitField('Submit')

#TODO add update form to edit/delete existing plants
'''
class UpdatePlantForm(FlaskForm):
    plant = SelectField('Plant') #dynamically populate choices based on which plants are assocaited with the user
    pot = StringField('Pot type', validators=[DataRequired()])
    watering_frequency = IntegerField('Watering Frequency (days)', validators=[DataRequired(), NumberRange(min=1, max = 60)])
    delete = BooleanField('Remove Plant?')
    watered = BooleanField('Watered Plant?')
    submit = SubmitField('Submit')
'''