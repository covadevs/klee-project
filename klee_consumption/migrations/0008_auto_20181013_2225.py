# Generated by Django 2.1.2 on 2018-10-13 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klee_consumption', '0007_consumption_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='description',
            field=models.TextField(default=None, max_length=30, null=True, verbose_name='Description'),
        ),
    ]
