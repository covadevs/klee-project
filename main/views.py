from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from klee_income.models import Income
from klee_income.tables import IncomeTable
from klee_consumption.models import Consumption
from klee_consumption.tables import ConsumptionTable
from klee_consumption.tables import ConsumptionFilter
from klee_consumption.tables import FilteredConsumptionListView
from django.db.models import Sum
from djmoney.models.fields import MoneyField
from djmoney.money import Money
import fontawesome as fa

# Create your views here.

@login_required
def main(request):
    context_dict = {
        'title': 'Klee'
    }
    
    return render(request, 'main/index.pug', context=context_dict)

@login_required
def incomes(request):
    income = Income.objects.filter(pk=request.user.id)

    if len(income) > 0:
        value = income[0].value
        sugested_value = (95/100)*value
    else:
        sugested_value = Money(0, 'R$')
        value = Money(0, 'R$')
    
    if(Consumption.objects.filter(pk=request.user.id).exists()):
        consumptions = Consumption.objects.filter(paid=False)
        if consumptions is not None:
            spent = Money(consumptions.aggregate(Sum('value'))['value__sum'], 'R$')
            reduction_value = spent-((95/100)*value)

            if reduction_value.amount < 0:
                reduction_value = Money(0, 'R$')
    else:
        spent = Money(0, 'R$')    
        reduction_value = Money(0, 'R$')
    

    if spent > value:
        message = "You spend more than you earn."
    elif value > spent and value.amount > 0:
        message = "You save money"
    elif value.amount == 0 and spent.amount == 0:
        message = "Você não possui gastos e receita"

    context_dict = {
        'title': 'Klee',
        'value': value,
        'spent': spent,
        'reduction_value': reduction_value,
        'sugested_value': sugested_value,
        'message': message,
    }

    return render(request, 'content/income-content.pug', context=context_dict)

@login_required
def consumptions(request):
    consumptionsUser = Consumption.objects.filter(user=request.user.id)
    filter = ConsumptionFilter(request.GET, queryset=consumptionsUser)

    table = ConsumptionTable(filter.qs)
    RequestConfig(request).configure(table)
    context_dict = {
        'table': table,
        'filter': filter,
        'title': 'Klee'
    }

    return render(request, 'content/consumption-content.pug', context=context_dict)