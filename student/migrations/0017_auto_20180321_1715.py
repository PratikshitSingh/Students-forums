# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 11:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20180321_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 17, 15, 9, 504064)),
        ),
    ]
