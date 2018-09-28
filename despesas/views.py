from django.shortcuts import render
from despesas.models import despesa
from despesas.forms import CriarDespesasForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def criarDespesas(request, id):
    user = User.objects.get(pk=id)

    if request.method == 'POST':
        form =criarDespesasForm(request.POST)
        
        if form.is_valid():
            value = form.cleaned_data['value']

            despesa = despesa(user=user, value=value)
            despesa.save()
            messages.success(request, 'Despesas Criadas!')
            return HttpResponseRedirect('/despesas')
    else:
        form = CriarDespesasForm()

    response = HttpResponse(form)

    return response