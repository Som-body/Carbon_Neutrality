# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20151121_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselslide',
            name='image',
            field=models.ImageField(default='Main/no_img.png', upload_to='Main'),
        ),
    ]
