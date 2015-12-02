# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0023_auto_20151130_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'ordering': ['-net_emission']},
        ),
        migrations.AddField(
            model_name='usermodel',
            name='net_emission',
            field=models.DecimalField(max_digits=16, default=Decimal('0.00'), decimal_places=2),
        ),
    ]
