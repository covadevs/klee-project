from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from datetime import datetime
from klee_category.models import Category
# Create your models here.

class Consumption(models.Model):

    WEEKLY  = 'W'
    MONTHLY = 'M'
    CONSUMPTION_CHOICES = (
        (WEEKLY, 'SEMANAL'),
        (MONTHLY, 'MENSAL')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category', related_name='system_category')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    value = MoneyField(max_digits=14, decimal_places=2, default_currency='R$')

    description = models.CharField('Description', max_length=30)

    date = models.DateField(null=False)

    paid = models.BooleanField(null=False, default=False)

    consumption_opts = models.CharField(
        'Expense type',
        max_length = 1,
        choices = CONSUMPTION_CHOICES,
        default = WEEKLY
    )

    def __repr__(self):
        return str(self.value)
