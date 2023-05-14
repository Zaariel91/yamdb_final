import re
from django.core.exceptions import ValidationError

USERNAME = re.compile(r'^[\w.@+-]+')


def validate_username(name):
    if name == 'me':
        raise ValidationError(
            'Имя пользователя "me" уже существует,введите другое имя'
        )
    if not USERNAME.fullmatch(name):
        raise ValidationError(
            'В названии имени можно использовать только буквы, цифры'
        )
