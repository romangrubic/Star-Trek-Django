# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-03 11:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200402_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='content',
            new_name='reply',
        ),
    ]
