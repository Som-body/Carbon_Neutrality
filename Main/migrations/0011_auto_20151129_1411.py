# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_auto_20151128_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='bus_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='car_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='clothes_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='drink_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='electricity_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='fuel_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='furniture_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='gas_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='general_meat_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='health_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='house_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='milk_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='motorcyle_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='plane_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='poultry_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='seafood_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='train_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='vegetable_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='vehicle_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='water_emissions',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
    ]
