from django.shortcuts import render

# Create your views here.

def login(request):
    context_dict = {
        'username': "Leonardo",
        'title': "Klee Login"
        }

    return render(request, 'login.jade', context=context_dict)

def createAccount(request):
    context_dict = {
        'title': 'Create a new Klee account'
    }

    return render(request, 'new-account.jade', context=context_dict)

