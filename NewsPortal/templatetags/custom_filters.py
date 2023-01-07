from django import template

register = template.Library()

CENSOR_WORDS = [
    'Редиска',
    'Жук',
    'Червяк'
]


@register.filter()
def censor(text):
    for word in CENSOR_WORDS:
        text = text.replace(word, '*' * len(word))
    return text
