from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def logout_klee(request):
    user = request.user
    if user is not None:
        if user.is_active:
            logout(request)
            return HttpResponseRedirect('/login')