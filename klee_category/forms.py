from django import forms
from django.forms import ModelForm
from .models import Category

class CreateCategoryForm(ModelForm):
    class Meta:
        model=Category
        fields = ['category_name', 'category_acron']