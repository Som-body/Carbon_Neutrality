# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_auto_20151129_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='longitude',
            field=models.DecimalField(max_digits=8, default=0, decimal_places=5),
            preserve_default=False,
        ),
    ]
