from django import forms
from django.forms import ModelForm
from .models import Consumption
from djmoney.models.fields import MoneyField
from djmoney.forms.widgets import MoneyWidget

class CreateConsumptionForm(ModelForm):
    class Meta:
        model=Consumption
        fields = ['value', 'consumption_opts', 'paid', 'category_opts', 'date']
        widgets = {
            'value': MoneyWidget(attrs={
                'placeholder': 'Consumption value',
                'min': '0.1',
                'step': '0.01',
                'type': 'number' 
            }),
        }
