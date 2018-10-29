from .models import Category
from klee_category import views
import django_tables2 as tables
from django.urls import reverse

class CategoryTable(tables.Table):    
    class Meta:
        model = Category
        
        row_attrs = {
            'data-id': lambda record: record.pk,
            'onclick': lambda record: 'tableRowClickCategory("'+reverse(views.getCategoryDetails,  kwargs={'categoryId':record.pk})+'")',
        }

        fields = ['category_name', 'category_acron']
        empty_text = 'No data'