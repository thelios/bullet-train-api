# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-17 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180517_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identity',
            name='hash',
        ),
    ]
