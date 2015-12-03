# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0035_auto_20151201_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='motorcycle_emissions',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='car_efficiency',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='fuel_emission',
            field=models.DecimalField(decimal_places=0, default=Decimal('8874'), max_digits=5),
        ),
    ]
