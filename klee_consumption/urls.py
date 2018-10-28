from django.urls import path
from klee_consumption import views

urlpatterns = [
    path('create-consumption', views.createConsumption, name='create-consumption'),
    path('expense-report', views.generateExpenseReport, name='expense-report'),
    path('expense-detail/<int:expenseId>', views.getExpenseDetails, name='expense-detail'),
    path('<int:expenseId>/expense-edit', views.edit, name='expense-edit'),
    path('<int:expenseId>/expense-delete', views.delete, name='expense-delete'),
]