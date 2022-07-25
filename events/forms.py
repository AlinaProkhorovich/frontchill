from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  TextAreaField, DateTimeField, FileField
from wtforms.validators import DataRequired


class EventForm(FlaskForm):
    title = StringField('Event', validators=[DataRequired(), ])
    description = TextAreaField('description', validators=[DataRequired(), ])
    date_event = DateTimeField('Дата проведения', validators=[DataRequired(), ])
    category = StringField('category', validators=[DataRequired(), ])
    place = StringField('place', validators=[DataRequired(), ])
    photo = FileField("photo", validators=[DataRequired(), ])
    price = StringField('price', validators=[DataRequired(), ])

    submit = SubmitField('Добавить мероприятие')



class CategoryForm(FlaskForm):

    name_category = StringField(' category', validators=[DataRequired(), ])

    submit = SubmitField('Добавить категорию')


class PlaceForm(FlaskForm):
    category = StringField('category', validators=[DataRequired(), ])
    event = StringField('Event', validators=[DataRequired(), ])
    place = StringField('place', validators=[DataRequired(), ])
    adress = StringField('place', validators=[DataRequired(), ])

    submit = SubmitField('Добавить место проведения')


class CommentForm(FlaskForm):
    comment = StringField("Комментарий к мероприятию", validators=[DataRequired(), ])

    submit = SubmitField("Оставить комментарий")

