from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from login.models import User_Profile
from login.forms import LoginForm
from login.forms import AccountForm
from django.contrib import messages

# Create your views here.
def login(request):
    user = request.user
    if user.is_active:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            login_form = form.cleaned_data['login']
            password_form = form.cleaned_data['senha']

            user = authenticate(username=login_form, password=password_form)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged succefully!')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Invalid user or password!')
    else:
        form = LoginForm()

    context_dict = {
        'title': 'Klee',
        'form': form
    }

    return render(request, 'login/login.pug', context=context_dict)

def createAccount(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        
        if form.is_valid():
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            new_user = User.objects.create_user(
                username=login, 
                email=email, 
                password=password)
            new_user.save()

            new_profile = User_Profile(user=new_user)
            new_profile.save()

            return HttpResponseRedirect('/login/')
    else:
        form = AccountForm()

    context_dict = {
        'form': form,
        'title': 'Create a new Klee account'
    }

    return render(request, 'login/new-account.jade', context=context_dict)


