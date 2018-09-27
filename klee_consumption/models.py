from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

# Create your models here.

class Consumption(models.Model):

    WEEKLY = 'S'
    MONTHLY = 'M'
    CONSUMPTION_CHOICES = (
        (WEEKLY, 'SEMANAL'),
        (MONTHLY, 'MENSAL')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    value = MoneyField(max_digits=14, decimal_places=4, default_currency='USD')

    consumption_opts = models.CharField(
        'Consumption type',
        max_length = 1,
        choices = CONSUMPTION_CHOICES,
        default = WEEKLY
    )
