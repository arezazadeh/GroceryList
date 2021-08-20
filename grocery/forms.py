from django import forms
from django.forms import ModelForm

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class GroceryListForm(ModelForm):

    class Meta:
        model = GroceryList
        fields = ['name', 'item', 'completed', 'date']
        widgets = {
            'made_on': DateInput(),
        }