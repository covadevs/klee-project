from django.shortcuts import render
from klee_consumption.models import Consumption
from klee_consumption.forms import CreateConsumptionForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from djmoney.money import Money
from klee_consumption.models import Consumption
from klee_income.models import Income
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import random

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
            description = form.cleaned_data['description']

            consumption = Consumption(user=user, value=value, description=description, consumption_opts=consumption_opts, date=date, paid=paid, category_opts=category_opts)
            consumption.save()
            messages.success(request, 'Consumption created!')
            return HttpResponseRedirect('/consumptions')
    else:
        form = CreateConsumptionForm()

    response = HttpResponse(form)

    return response

@login_required
def generateExpenseReport(request):
    try:
        userId = request.user.id

        income = Income.objects.get(user=userId)
        expenses = Consumption.objects.filter(user=userId)
        balances = []

        totalExpenseAmount = Money(0, 'R$')
        balance = income.value
        for expense in expenses:
            if(expense.paid == False):
                balance = balance - expense.value
            balances.append(balance)
            totalExpenseAmount += expense.value

        finalBalance = Money(0, 'R$')
        for balance in balances:
            finalBalance += balance

        rpRandomNumber = random.randint(1000, 2000)

            

        context_dict = {
            'title': 'Klee - Expense Report',
            'income': income,
            'expenses': expenses,
            'balances': balances,
            'finalBalance': finalBalance,
            'totalExpenseAmount': totalExpenseAmount,
            'rpRandomNumber': rpRandomNumber,
            'exists': True
        }
    except ObjectDoesNotExist:
        context_dict = {
            'exists': False
        }

    return render(request, 'klee-consumption/expense-report.pug', context=context_dict)


    
