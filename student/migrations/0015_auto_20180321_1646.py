# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 11:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20180321_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 46, 5, 831336)),
        ),
    ]
