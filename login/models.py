from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.email