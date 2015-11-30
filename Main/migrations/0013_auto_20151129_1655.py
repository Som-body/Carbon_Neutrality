# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_auto_20151129_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tree',
            old_name='location_name',
            new_name='location',
        ),
    ]
