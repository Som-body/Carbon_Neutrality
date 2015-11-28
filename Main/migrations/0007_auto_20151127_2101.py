# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
