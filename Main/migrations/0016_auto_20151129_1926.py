# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_tree_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='species',
            field=models.CharField(max_length=50),
        ),
    ]
