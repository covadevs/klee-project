from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consumption(models.Model):

    WEEKLY = 'S'
    MONTHLY = 'M'
    CONSUMPTION_CHOICES = (
        (WEEKLY, 'SEMANAL'),
        (MONTHLY, 'MENSAL')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    value = models.DecimalField(max_digits=19, decimal_places=2)

    consumption_opts = models.CharField(
        max_length = 1,
        choices = CONSUMPTION_CHOICES,
        default = WEEKLY
    )
