from flask_wtf import Form
from wtforms import TextField, IntegerField, PasswordField, FileField, DecimalField, StringField, SubmitField, RadioField
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename


class RegisterForm(Form):
    name = TextField('name', validators=[DataRequired()])

    email = TextField('Email', validators=[DataRequired(), Email()])  

    password = PasswordField('Password', validators=[DataRequired()])

    confirm = PasswordField('Repeat Password',[DataRequired(),EqualTo('password', message='Passwords must match')])

    user_type = RadioField('user_type', choices=[('value1', 'Farmer'), ('value2', 'Wholeseller'), ('value3', 'Retailer'), ('value4','Civilian')], 
        validators=[DataRequired()])

    submit = SubmitField('Register')
        
    #upload = FileField('image', validators=[FileAllowed(['jpg'],'Upload your picture')])


class LoginForm(Form):
    user_id = IntegerField('user id', [DataRequired()])

    name = TextField('name', [DataRequired()])

    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    email = TextField('Email', validators=[DataRequired(), Length(min=6, max=40)])


class UploadForm(Form):
    WholesellerName = TextField('Seller Name',validators=[DataRequired(), Length(min=6, max=40)])

    VegetableName = TextField('Veggies', validators=[DataRequired(), Length(min=6, max=40)]) 
    
    Price = DecimalField('Price per Kilo',[DataRequired()])


class RegisterComplaintForm(Form):
    title = TextField('title', validators=[DataRequired()])

    category = TextField('category', validators=[DataRequired()])


    #upload = FileField('image', validators=[FileAllowed(['jpg'],'Upload your veggies')])