from django.urls import path
from klee_consumption import views

urlpatterns = [
    path('create-consumption', views.createConsumption, name='create-consumption'),
    path('expense-report', views.generateExpenseReport, name='expense-report'),
]