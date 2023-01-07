from django_filters import widgets, FilterSet, DateFilter
from django import forms
from .models import *


class NewsFilter(FilterSet):
    pub_time = DateFilter(
        field_name='pub_time',
        label='Опубликовано с:',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'DD/MM/YYYY',
            }
        ),
    )

    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'author': ['exact'],
       }