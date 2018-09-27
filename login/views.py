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
        'title': 'Klee - Taking good care of your money',
        'form': form
    }

    return render(request, 'login/login.pug', context=context_dict)

def createAccount(request):
    if request.method == 'POST':
        form_new = AccountForm(request.POST)
        
        if form_new.is_valid():
            login = form_new.cleaned_data['login']
            email = form_new.cleaned_data['email']
            password = form_new.cleaned_data['password']

            if not User.objects.filter(username=login).exists():
                if not User.objects.filter(email=email).exists():
                    new_user = User.objects.create_user(
                        username=login, 
                        email=email, 
                        password=password)
                    new_user.save()

                    new_profile = User_Profile(user=new_user)
                    new_profile.save()

                    messages.success(request, 'Your account has been created!')
                    return HttpResponseRedirect('/login/')
                else :
                    messages.error(request, 'Email already exists')
            else:
                messages.error(request, 'Username already exists')
    else:
        form_new = AccountForm()

    context_dict = {
        'form_new': form_new,
        'title': 'Create a new Klee account'
    }

    return render(request, 'login/new-account.jade', context=context_dict)

# def editUserAccount(request, userId):


