# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0017_auto_20151129_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tree',
            old_name='img',
            new_name='picture',
        ),
    ]
