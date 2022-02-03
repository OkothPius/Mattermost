from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class GameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    viewer_hour = IntegerField('Viewer Hours', validators=[DataRequired()])
    hours_streamed = IntegerField('Viewer Hours', validators=[DataRequired()])
    acv_num = IntegerField('ACV', validators=[DataRequired()])
    creators = IntegerField('Creators', validators=[DataRequired()])
    streams_num = IntegerField('Numbers Streamed', validators=[DataRequired()])
    submit = SubmitField('Submit')
