# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0020_auto_20151129_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='date_died',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
