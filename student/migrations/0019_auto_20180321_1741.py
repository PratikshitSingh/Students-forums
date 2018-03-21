# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 12:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20180321_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='hostel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Hostel_name'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 17, 41, 2, 226640)),
        ),
    ]