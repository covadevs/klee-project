from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from login.models import User_Profile
from user.forms import EditUserForm
from user.forms import ChangePasswordForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def editUser(request, id):
    user = User.objects.get(pk=id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        form.save()
        messages.success(request, 'Profile edited!')
        return HttpResponseRedirect('/')
    else:
        form = EditUserForm(instance=user)

    response = HttpResponse(form)

    return response

def changePassword(request, id):
    user = User.objects.get(pk=id)

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']

        if password == user.password:
            if password != new_password:
                user.set_password(new_password)
                user.save()

                messages.success(request, 'Password changed!')
                return HttpResponseRedirect('/')
            else :
                messages.error(request, 'Same password!')
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Wrong password!')
            return HttpResponseRedirect('/')

    else:
        form = ChangePasswordForm()

    response = HttpResponse(form)

    return response
