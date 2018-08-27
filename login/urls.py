from django.urls import path
from login import views

urlpatterns = [
    path('', views.login),
    path('new-account', views.createAccount),
]