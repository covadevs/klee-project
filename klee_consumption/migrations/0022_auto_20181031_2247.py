# Generated by Django 2.1.2 on 2018-10-31 22:47

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('klee_consumption', '0021_auto_20181028_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='value',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency='R$', max_digits=14),
        ),
        migrations.AlterField(
            model_name='consumption',
            name='value_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('R$', 'Real')], default='R$', editable=False, max_length=3),
        ),
    ]
