from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired


class ImageForm(FlaskForm):
    img = FileField('Image', validators=[FileRequired()])
