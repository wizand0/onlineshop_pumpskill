from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, FileField
from wtforms.validators import DataRequired


class BrandUpdateForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])


class ItemCreationForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired()])
    brand = SelectField('brand', choices=[])


class ItemUpdateForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired()])
    logo = FileField()


class AddToCartForm(FlaskForm):
    pass