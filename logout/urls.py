from django.urls import path
from logout import views

urlpatterns = [
    path('', views.logout_klee, name='logout'),
]