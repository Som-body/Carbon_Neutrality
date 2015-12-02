# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0024_auto_20151130_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date_friended', models.DateTimeField()),
                ('friend', models.ForeignKey(related_name='main_friend_friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='friends',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='user',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('user', 'friend')]),
        ),
    ]
