from django import forms
from django.forms import ModelForm
from .models import Category

class CreateCategoryForm(ModelForm):
    category_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Category name'
    }))
    category_acron = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Acron',
        'maxlength': '2'
    }))
    class Meta:
        model=Category
        fields = ['category_name', 'category_acron']