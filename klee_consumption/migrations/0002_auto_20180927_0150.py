# Generated by Django 2.1 on 2018-09-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klee_consumption', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='consumption_opts',
            field=models.CharField(choices=[('S', 'SEMANAL'), ('M', 'MENSAL')], db_column='Choice', default='S', max_length=1),
        ),
    ]