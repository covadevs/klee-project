from django import forms

class CriarDespesasForm(forms.Form):
    value = forms.DecimalField(max_digits=19, decimal_places=2, label='',
    widget=forms.TextInput(attrs={
        'placeholder': 'Despesas Valor',
        'autofocus': 'true'
        }))