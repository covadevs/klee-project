from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from login.models import User_Profile
from user.forms import EditUserForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def editUser(request, id):
    user = User.objects.get(pk=id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = EditUserForm(instance=user)

    response = HttpResponse(form)

    return response