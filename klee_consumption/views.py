from django.shortcuts import render
from klee_consumption.models import Consumption
from klee_consumption.forms import CreateConsumptionForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def createConsumption(request):
    userId = request.user.id
    user = User.objects.get(pk=userId)

    if request.method == 'POST':
        form = CreateConsumptionForm(request.POST)
        
        if form.is_valid():
            value = form.cleaned_data['value']
            consumption_opts = form.cleaned_data['consumption_opts']

            consumption = Consumption(user=user, value=value, consumption_opts=consumption_opts)
            consumption.save()
            messages.success(request, 'Consumption created!')
            return HttpResponseRedirect('/consumptions')
    else:
        form = CreateConsumptionForm()

    response = HttpResponse(form)

    return response