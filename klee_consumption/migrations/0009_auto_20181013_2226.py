# Generated by Django 2.1.2 on 2018-10-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klee_consumption', '0008_auto_20181013_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='description',
            field=models.TextField(max_length=30, verbose_name='Description'),
        ),
    ]
