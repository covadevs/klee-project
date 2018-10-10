from django.shortcuts import render
from klee_consumption.models import Consumption
from klee_consumption.forms import CreateConsumptionForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

def createConsumption(request):
    userId = request.user.id
    user = User.objects.get(pk=userId)

    if request.method == 'POST':
        form = CreateConsumptionForm(request.POST)
        
        if form.is_valid():
            value = form.cleaned_data['value']
            consumption_opts = form.cleaned_data['consumption_opts']
            category_opts = form.cleaned_data['category_opts']
            date = form.cleaned_data['date']
            paid = form.cleaned_data['paid']

            consumption = Consumption(user=user, value=value, consumption_opts=consumption_opts, date=date, paid=paid, category_opts=category_opts)
            consumption.save()
            messages.success(request, 'Consumption created!')
            return HttpResponseRedirect('/consumptions')
    else:
        form = CreateConsumptionForm()

    response = HttpResponse(form)

    return response

def generateConsumptionsPDF(request):
    userId = request.user.id

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(100, 100, "Hello world.")

    p.showPage()
    p.save()

    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
