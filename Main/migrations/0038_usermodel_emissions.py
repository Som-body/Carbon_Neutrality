# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0037_auto_20151203_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='emissions',
            field=models.DecimalField(max_digits=16, decimal_places=2, default=Decimal('0.00')),
        ),
    ]
