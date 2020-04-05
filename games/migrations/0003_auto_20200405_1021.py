# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-05 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200401_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='link',
            new_name='game_link',
        ),
        migrations.AddField(
            model_name='games',
            name='forum_thread',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
