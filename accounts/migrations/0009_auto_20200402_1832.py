# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-02 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200402_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='reciever',
            new_name='receiver',
        ),
    ]