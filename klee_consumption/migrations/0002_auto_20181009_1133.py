# Generated by Django 2.1.2 on 2018-10-09 11:33

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('klee_consumption', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='value_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BRL', 'Brazilian Real')], default='BRL', editable=False, max_length=3),
        ),
    ]
