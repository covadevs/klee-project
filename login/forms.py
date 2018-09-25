from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=50, label='',
    widget=forms.TextInput(attrs={
        'placeholder': 'Username or email',
        'autofocus': 'true'
        }))
    senha = forms.CharField(max_length=50,
    widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'}), label='')

class AccountForm(forms.Form):
    login = forms.CharField(
        max_length=50, 
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Username'
        }))
    
    email = forms.EmailField(
        label='',
        widget = forms.EmailInput(attrs={
        'placeholder': 'Email',
        'autocomplete': 'off'
    }))

    password = forms.CharField(
        max_length=50,
        label = '',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'autocomplete': 'off'
        }))

class RecoverForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget = forms.EmailInput(attrs={
        'placeholder': 'Email',
        'autocomplete': 'off'
    }))