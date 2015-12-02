# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0027_auto_20151201_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='date_friended',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 2, 56, 51, 662098, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tree',
            name='picture',
            field=models.ImageField(upload_to='trees', default='trees/tree101.png'),
        ),
    ]
