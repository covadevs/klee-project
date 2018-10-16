from django.shortcuts import render
from .models import Category
from .forms import CreateCategoryForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def createCategory(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['category_name']
            acron = form.cleaned_data['category_acron']

            category = Category(category_name=name, category_acron=acron)
            category.save()
            messages.success(request, 'Category created!')
            return HttpResponseRedirect('/consumptions')
    else:
        form = CreateCategoryForm()

    response = HttpResponse(form)

    return response