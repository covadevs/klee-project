from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class ChangePasswordForm(forms.Form):
        password = forms.CharField(
        max_length=50,
        label = '',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'autofocus': 'true'
        }))

        new_password = forms.CharField(
        max_length=50,
        label = '',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'New password',
            'autocomplete': 'off'
        }))