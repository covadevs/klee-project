from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from datetime import datetime
# Create your models here.

class Consumption(models.Model):

    WEEKLY  = 'W'
    MONTHLY = 'M'
    CONSUMPTION_CHOICES = (
        (WEEKLY, 'SEMANAL'),
        (MONTHLY, 'MENSAL')
    )

    OTHERS              = 'OT'
    NOCATEGORY          = 'NC'
    HOME                = 'HM'
    EDUCATION           = 'ED'
    RECREATION          = 'RT'
    FOOD                = 'FD'
    TRANSPORT           = 'TP'
    PERSONALEXPENSES    = 'PE'
    COMMUNICATION       = 'CM'
    RATESANDTAXES       = 'RT'
    HEALTH              = 'HT'
    CONSUMPTION_CATEGORY = (
        (OTHERS, 'OTHERS'),
        (NOCATEGORY, 'NO CATEGORY'),
        (HOME, 'HOME'),
        (EDUCATION, 'EDUCATION'),
        (RECREATION, 'RECREATION'),
        (FOOD, 'FOOD'),
        (TRANSPORT, 'TRANSPORT'),
        (PERSONALEXPENSES, 'PERSONAL EXPENSES'),
        (COMMUNICATION, 'COMMUNICATION'),
        (RATESANDTAXES, 'RATES AND TAXES'),
        (HEALTH, 'HEALTH'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    value = MoneyField(max_digits=14, decimal_places=4, default_currency='BRL')

    description = models.CharField('Description', max_length=30)

    date = models.DateField(null=False)

    paid = models.BooleanField(null=False, default=False)

    consumption_opts = models.CharField(
        'Expense type',
        max_length = 1,
        choices = CONSUMPTION_CHOICES,
        default = WEEKLY
    )

    category_opts = models.CharField(
        'Category',
        max_length = 2,
        choices = CONSUMPTION_CATEGORY,
        default = NOCATEGORY
    )

    def __repr__(self):
        return str(self.value)
