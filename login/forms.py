from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=50, label='',
    widget=forms.TextInput(attrs={
        'placeholder': 'Username or email'}))
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
    
    email = forms.EmailField()

    password = forms.CharField(
        max_length=50,
        label = '',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )