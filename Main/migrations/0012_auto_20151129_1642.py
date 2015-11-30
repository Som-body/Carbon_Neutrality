# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_auto_20151129_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tree',
            old_name='tree_date_planted',
            new_name='date_planted',
        ),
        migrations.RenameField(
            model_name='tree',
            old_name='tree_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='tree',
            old_name='tree_is_alive',
            new_name='is_alive',
        ),
        migrations.RenameField(
            model_name='tree',
            old_name='tree_location_name',
            new_name='location_name',
        ),
        migrations.RenameField(
            model_name='tree',
            old_name='tree_species',
            new_name='species',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='tree_adult_diameter',
        ),
        migrations.AddField(
            model_name='tree',
            name='adult_diameter',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
    ]
