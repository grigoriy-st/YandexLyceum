from flask_wtf import FlaskForm
from wtforms import EmailField, StringField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    creator = StringField('Creator', validators=[DataRequired])
    title = StringField('Title of department', validators=[DataRequired()])
    chief = StringField('Chief', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
