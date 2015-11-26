# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20151121_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselslide',
            name='image',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]
