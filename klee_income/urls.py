from django.urls import path
from klee_income import views

urlpatterns = [
    path('create-income', views.createIncome, name='create-income'),
]