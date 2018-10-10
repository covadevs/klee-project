import django_tables2 as tables
import django_filters
from klee_consumption.models import Consumption
from django_filters.views import FilterView
from django_filters.widgets import RangeWidget
from django_filters import DateFromToRangeFilter
from django_tables2.views import SingleTableMixin
from djmoney.models.fields import MoneyField

class MyRangeWidget(RangeWidget):
    def __init__(self, from_attrs=None, to_attrs=None, attrs=None):
        super(MyRangeWidget, self).__init__(attrs)

        if from_attrs:
            self.widgets[0].attrs.update(from_attrs)
        if to_attrs:
            self.widgets[1].attrs.update(to_attrs)

class ConsumptionTable(tables.Table):
    class Meta:
        model = Consumption
        fields = ['value', 'consumption_opts', 'paid', 'category_opts', 'date']
        empty_text = 'No data'

class ConsumptionFilter(django_filters.FilterSet):
    date = DateFromToRangeFilter(
        widget=(
            MyRangeWidget(
                from_attrs={
                    'placeholder': 'Min date'
                },
                to_attrs={
                    'placeholder': 'Max date'
                }
    )))
    class Meta:
        model = Consumption
        fields = ['value', 'consumption_opts', 'paid', 'category_opts', 'date']

class FilteredConsumptionListView(SingleTableMixin, FilterView):
    table_class = ConsumptionTable
    model = Consumption
    filterset_class = ConsumptionFilter

