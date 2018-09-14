import django_tables2 as tables
from klee_income.models import Income

class IncomeTable(tables.Table):
    class Meta:
        model = Income
        template_name = 'django_tables2/bootstrap.html'