from django.shortcuts import render


# Create your views here.

def main(request):
    context_dict = {
        'title': 'Klee'
    }
    
    return render(request, 'main/index.pug', context=context_dict)

