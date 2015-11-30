# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20151128_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tree_adult_diameter', models.IntegerField()),
                ('tree_location_name', models.CharField(max_length=255)),
                ('tree_species', models.CharField(max_length=255)),
                ('tree_date_planted', models.DateTimeField()),
                ('tree_is_alive', models.BooleanField(default=True)),
                ('tree_img', models.ImageField(upload_to='/trees', default='pictures/tree101.png')),
                ('user', models.ForeignKey(to='Main.UserModel')),
            ],
        ),
    ]
