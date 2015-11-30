# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0019_auto_20151129_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tree',
            options={'ordering': ['-date_planted']},
        ),
    ]
