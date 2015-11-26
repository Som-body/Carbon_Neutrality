# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselslide',
            name='testext',
        ),
        migrations.AddField(
            model_name='carouselslide',
            name='image',
            field=models.ImageField(default='Main/pictures/no_img.png', upload_to='Main/pictures'),
        ),
        migrations.AddField(
            model_name='carouselslide',
            name='url',
            field=models.CharField(max_length=255, default=''),
        ),
    ]
