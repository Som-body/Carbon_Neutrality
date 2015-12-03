# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0034_auto_20151201_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'ordering': ['net_emission']},
        ),
    ]
