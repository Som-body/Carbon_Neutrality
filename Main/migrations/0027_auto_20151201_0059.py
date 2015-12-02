# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0026_auto_20151130_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='date_friended',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 1, 10, 59, 53, 701821, tzinfo=utc)),
        ),
    ]
