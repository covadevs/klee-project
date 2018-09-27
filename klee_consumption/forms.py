from django import forms
from django.forms import ModelForm
from .models import Consumption

class CreateConsumptionForm(ModelForm):
    class Meta:
        model=Consumption
        fields = ['value', 'consumption_opts']
        widgets = {
            'value': forms.NumberInput(attrs={'autofocus': 'true', 'placeholder': 'Consumption value'}),
        }
