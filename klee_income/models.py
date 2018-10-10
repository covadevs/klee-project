from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
# Create your models here.

class Income(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    value = MoneyField(max_digits=14, decimal_places=4, default_currency='R$')

    def __repr__(self):
        return str(self.value)

    def setValue(self, value):
        self.value = value
