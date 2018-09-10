from django.urls import path
from user import views

urlpatterns = [
    path('<int:id>/edit', views.editUser, name='edit-user')
]