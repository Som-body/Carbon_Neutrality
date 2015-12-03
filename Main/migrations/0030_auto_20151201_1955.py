# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0029_auto_20151201_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='date_friended',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
