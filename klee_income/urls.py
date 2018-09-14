from django.urls import path
from klee_income import views

urlpatterns = [
    path('create-income?userId=<int:id>', views.createIncome, name='create-income'),
]