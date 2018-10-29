from django.shortcuts import render
from .models import Category
from .forms import CreateCategoryForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.core.serializers import serialize
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

def getCategoryDetails(response, categoryId):
    category = Category.objects.filter(pk=categoryId)

    categories = serialize('json', category)
    link = ',{"link":"'+str(reverse(edit,  kwargs={'categoryId':categoryId}))

    linkdel = ',{"link":"'+str(reverse(delete,  kwargs={'categoryId':categoryId}))

    categories = categories[:-1] + link + '"}' + linkdel + '"}]'

    return HttpResponse(categories, content_type='application/json')

def edit(request, categoryId):
    print(categoryId)
    category = Category.objects.get(pk=categoryId)

    if(request.method == 'POST'):
        form = CreateCategoryForm(request.POST, instance=category)
        form.save()
        return HttpResponseRedirect('/categories')
    else:
        form = CreateCategoryForm(instance=category)
    return HttpResponse(form)

def delete(request, categoryId):
    category = Category.objects.get(pk=categoryId)
    
    category.delete()
    
    return HttpResponseRedirect('/categories')