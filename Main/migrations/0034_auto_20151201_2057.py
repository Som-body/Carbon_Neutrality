# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0033_auto_20151201_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='info'),
        ),
    ]
