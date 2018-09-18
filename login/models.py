from django.db import models
from django.contrib.auth.models import User
from klee_income.models import Income
# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username