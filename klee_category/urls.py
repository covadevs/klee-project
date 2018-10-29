from django.urls import path
from klee_category import views

urlpatterns = [
        path('create-category', views.createCategory, name='create-category'),
        path('category-detail/<int:categoryId>', views.getCategoryDetails, name='category-detail'),
        path('<int:categoryId>/category-edit', views.edit, name='category-edit'),
        path('<int:categoryId>/category-delete', views.delete, name='category-delete'),
]