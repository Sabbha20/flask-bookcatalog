from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    book_format = StringField('Format: ', validators=[DataRequired()])
    num_pages = StringField('Pages: ', validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateBookForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    author = StringField('Author: ', validators=[DataRequired()])
    avg_rating = FloatField('Rating: ', validators=[DataRequired()])
    img_url = StringField('Image URL: ', validators=[DataRequired()])
    book_format = StringField('Format: ', validators=[DataRequired()])
    num_pages = StringField('Pages: ', validators=[DataRequired()])
    pub_id = IntegerField('Publication Id: ', validators=[DataRequired()])
    submit = SubmitField('Create Book')