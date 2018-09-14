from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    value = models.DecimalField(max_digits=19, decimal_places=2)

    def __repr__(self):
        return str(self.value)
