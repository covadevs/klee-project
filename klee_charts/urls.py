from django.urls import path
from klee_charts import views

urlpatterns = [
        path('show-charts', views.showCharts, name='show-charts')
]