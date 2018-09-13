from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def main(request):
    context_dict = {
        'title': 'Klee'
    }
    
    return render(request, 'main/index.pug', context=context_dict)

@login_required
def settings(request):
    context_dict = {
        'title': 'Klee'
    }
    return render(request, 'content/settings.pug', context=context_dict)

