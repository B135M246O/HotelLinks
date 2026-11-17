from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import LINK_REG


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Ссылка на меню, правила, маршрут или контакты',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректная ссылка')]
    )
    custom_id = StringField(
        'Короткое имя, например menu или wifi',
        validators=[
            Optional(),
            Length(1, 16),
            Regexp(
                regex=LINK_REG,
                message='Допустимы только цифры и буквы "a-Z"')]
    )
    submit = SubmitField('Создать')
