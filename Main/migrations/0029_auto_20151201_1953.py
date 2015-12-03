# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0028_auto_20151201_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='date_friended',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 5, 53, 48, 968461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user',
            field=models.OneToOneField(related_name='info', to=settings.AUTH_USER_MODEL),
        ),
    ]
