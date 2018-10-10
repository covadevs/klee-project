from django import forms
from django.forms import ModelForm
from klee_income.models import Income
from djmoney.forms.widgets import MoneyWidget

class CreateIncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['value']
        widgets = {
            'value': MoneyWidget(attrs={
                'placeholder': 'Income value',
                'min': '0.1',
                'step': '0.01',
                'type': 'number',
            })
        }