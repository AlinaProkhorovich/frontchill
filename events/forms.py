from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  TextAreaField, DateTimeField, FileField,IntegerField
from wtforms.validators import DataRequired


class EventForm(FlaskForm):
    title = StringField('Event', validators=[DataRequired(), ])
    description = TextAreaField('description', validators=[DataRequired(), ])
    date_event = DateTimeField('Дата проведения', validators=[DataRequired(), ])
    category = StringField('category', validators=[DataRequired(), ])
    place = StringField('place', validators=[DataRequired(), ])
    photo = FileField("photo", validators=[DataRequired(), ])
    price = StringField('price', validators=[DataRequired(), ])
    age_limit = IntegerField ('Возрастное ограничение', validators=[DataRequired(), ])

    submit = SubmitField('Добавить мероприятие')

#
# class CommentForm(FlaskForm):
#     comment = StringField("Комментарий к мероприятию", validators=[DataRequired(), ])
#
#     submit = SubmitField("Оставить комментарий")