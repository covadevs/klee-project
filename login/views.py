from django.shortcuts import render

# Create your views here.

def login(request):
    context_dict = {
        'username': "Leonardo",
        'title': "Klee Login"
        }

    return render(request, 'login.jade', context=context_dict)
