# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0030_auto_20151201_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'ordering': ['-friend']},
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
