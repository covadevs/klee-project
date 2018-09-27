import django_tables2 as tables
from klee_consumption.models import Consumption

class ConsumptionTable(tables.Table):
    class Meta:
        model = Consumption
        fields = ['value', 'consumption_opts']
        empty_text = 'No data'