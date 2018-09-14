from django.shortcuts import render
from klee_income.models import Income
from klee_income.forms import CreateIncomeForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def createIncome(request, id):
    user = User.objects.get(pk=id)

    if request.method == 'POST':
        form = CreateIncomeForm(request.POST)
        
        if form.is_valid():
            value = form.cleaned_data['value']

            income = Income(user=user, value=value)
            income.save()
            messages.success(request, 'Income created!')
            return HttpResponseRedirect('/')
    else:
        form = CreateIncomeForm()

    response = HttpResponse(form)

    return response