from django.urls import path
from main import views

urlpatterns = [
    path('', views.main, name='main'),
    path('incomes', views.incomes, name='incomes'),
    path('consumptions', views.consumptions, name='consumptions'),
    path('categories', views.categories, name='categories'),
    path('charts', views.charts, name='charts'),
]