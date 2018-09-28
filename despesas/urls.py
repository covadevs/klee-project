from django.urls import path
from despesas import views

urlpatterns = [
    path('criar-despesas?userId=<int:id>', views.criarDespesas, name='criar-despesas'),
]