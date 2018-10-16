from django.urls import path
from klee_category import views

urlpatterns = [
        path('create-category', views.createCategory, name='create-category')
]