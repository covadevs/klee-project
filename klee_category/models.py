from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField('Category', max_length=20)
    category_acron = models.CharField('Category acronym', max_length=2)

    def __repr__(self):
        return str(self.category_name)

    def __str__(self):
        return str(self.category_name)
