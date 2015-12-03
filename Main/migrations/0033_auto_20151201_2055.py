# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0032_auto_20151201_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'ordering': ['friend_model']},
        ),
    ]
