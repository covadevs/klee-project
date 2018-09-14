from django import forms

class CreateIncomeForm(forms.Form):
    value = forms.DecimalField(max_digits=19, decimal_places=2, label='',
    widget=forms.TextInput(attrs={
        'placeholder': 'Income value',
        'autofocus': 'true'
        }))