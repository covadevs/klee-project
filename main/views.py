from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from klee_income.models import Income
from klee_income.tables import IncomeTable
from klee_consumption.models import Consumption
from klee_consumption.tables import ConsumptionTable

# Create your views here.

@login_required
def main(request):
    context_dict = {
        'title': 'Klee'
    }
    
    return render(request, 'main/index.pug', context=context_dict)

@login_required
def incomes(request):
    table = IncomeTable(Income.objects.filter(pk=request.user.id))
    RequestConfig(request).configure(table)

    context_dict = {
        'table': table,
        'title': 'Klee'
    }
    return render(request, 'content/income-content.pug', context=context_dict)

@login_required
def consumptions(request):
    table = ConsumptionTable(Consumption.objects.filter(user=request.user.id))
    RequestConfig(request).configure(table)
    print(table)
    context_dict = {
        'table': table,
        'title': 'Klee'
    }

    return render(request, 'content/consumption-content.pug', context=context_dict)