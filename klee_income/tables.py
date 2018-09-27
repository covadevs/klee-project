import django_tables2 as tables
from klee_income.models import Income

class IncomeTable(tables.Table):
    class Meta:
        model = Income
        fields = ['value']
        empty_text = 'No data'