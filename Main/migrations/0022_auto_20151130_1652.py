# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0021_tree_date_died'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='motorcyle_emissions',
            new_name='motorcycle_emissions',
        ),
    ]
