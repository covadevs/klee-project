from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from klee_income.models import Income
from klee_income.tables import IncomeTable
from klee_category.models import Category
from klee_category.tables import CategoryTable
from klee_consumption.models import Consumption
from klee_consumption.tables import ConsumptionTable
from klee_consumption.tables import ConsumptionFilter
from klee_consumption.tables import FilteredConsumptionListView
from django.db.models import Sum
from djmoney.models.fields import MoneyField
from djmoney.money import Money
import json
from django.db.models import Count

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
    
    if(Consumption.objects.filter(user=request.user.id).exists()):
        consumptions = Consumption.objects.filter(paid=False)
        if len(consumptions) > 0:
            spent = Money(consumptions.aggregate(Sum('value'))['value__sum'], 'R$')
            reduction_value = spent-((95/100)*value)

            if reduction_value.amount < 0:
                reduction_value = Money(0, 'R$')
        else:
            spent = Money(0, 'R$')
            reduction_value = Money(0, 'R$')
    else:
        spent = Money(0, 'R$')
        reduction_value = Money(0, 'R$')
        
    if spent > value:
        message = "You spend more than you earn."
    elif value > spent and value.amount > 0:
        message = "You save money"
    elif value.amount == 0 and spent.amount == 0:
        message = "You have no expenses and revenue"
    elif value == spent:
        message = "Limit reached"

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
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    context_dict = {
        'table': table,
        'filter': filter,
        'title': 'Klee'
    }

    return render(request, 'content/consumption-content.pug', context=context_dict)

@login_required
def categories(request):
    category = Category.objects.all()

    table = CategoryTable(category)
    RequestConfig(request).configure(table)
    context_dict = {
        'title': 'Klee',
        'table': table
    }

    return render(request, 'content/category-content.pug', context=context_dict)

@login_required
def charts(request) :
    queryset = Consumption.objects.filter(user=request.user.id)
    querysetCategory = Consumption.objects.values('category').order_by('category').annotate(count=Count('category'))
    categories = Category.objects.all().order_by('pk')

    paids = [obj.paid for obj in queryset]
    values = [str(obj.value.amount) for obj in queryset]
    dates = [str(obj.date) for obj in queryset]
    type = [str(obj.consumption_opts) for obj in queryset]
    count_by_categories = [obj['count'] for obj in querysetCategory]
    categories = [obj.category_name for obj in categories]
    print(categories)

    context_dict = {
        'title': 'Klee',
        'paids': json.dumps(paids),
        'values': json.dumps(values),
        'dates': json.dumps(dates),
        'types': json.dumps(type),
        'categories_count': json.dumps(count_by_categories),
        'categories': json.dumps(categories)
    }



    return render(request, 'content/chart-content.pug', context=context_dict)