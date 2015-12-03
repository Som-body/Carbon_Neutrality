# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0031_auto_20151201_2043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'ordering': ['-friend_model']},
        ),
        migrations.AddField(
            model_name='friend',
            name='friend_model',
            field=models.ForeignKey(null=True, to='Main.UserModel'),
        ),
    ]
