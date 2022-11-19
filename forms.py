from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import DateField, SubmitField, IntegerField, FloatField , StringField, PasswordField, BooleanField, SelectField, SelectMultipleField, widgets, validators
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo, InputRequired
import datetime
import email_validator

class Productform(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3,max=20)] )
    description = StringField('Description', validators=[DataRequired(), Length(min=3,max=20)] )
    category = StringField('Category', validators=[DataRequired(), Length(min=3,max=20)] )
    price = FloatField('Price')
    quantity = IntegerField('Quantity available')
    availability = BooleanField('The product is available')
    prod_picture = FileField('Add a picture')
    submit=SubmitField('Add')

class Signup(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3,max=20)] )
    surname = StringField('Surname', validators=[DataRequired(), Length(min=3,max=20)] )
    email = StringField('Email', validators=[DataRequired(), Email()])
    # tel = StringField('Phone Number')
    # dob = DateField('Date of Birth')
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, max=22)])
    confirm = PasswordField('Confirm Password', validators=[EqualTo('password', message='Passwords must match' )])
    # accept_tos = BooleanField('I accept the Terms of Subscription', validators=[DataRequired()])
    # age = BooleanField('I am 18 years old or over', validators=[DataRequired()])
    submit = SubmitField('Confirm')

    # def validate_email(self,email):
    #     user_check=User.query.filter_by(username=self.email.data).first()
    #     if user_check:
    #         raise ValidationError('This user has been register before or taken')


class Signin(FlaskForm):
    username=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[Length(min=3,max=15),DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit=SubmitField('Login')

