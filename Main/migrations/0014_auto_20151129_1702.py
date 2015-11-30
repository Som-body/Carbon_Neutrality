# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_auto_20151129_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='latitude',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tree',
            name='adult_diameter',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
