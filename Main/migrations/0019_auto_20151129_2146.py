# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0018_auto_20151129_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='date_planted',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tree',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
