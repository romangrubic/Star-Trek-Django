# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-29 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200329_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cosplay_input',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favourite_quote',
            field=models.TextField(max_length=500),
        ),
    ]
