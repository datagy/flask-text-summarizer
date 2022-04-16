from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class SubmitTextForm(FlaskForm):
    text = TextAreaField('Text to Summarize', validators=[DataRequired()])
    submit = SubmitField('Submit')