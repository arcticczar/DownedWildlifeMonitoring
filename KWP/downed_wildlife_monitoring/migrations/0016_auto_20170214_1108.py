# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 21:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downed_wildlife_monitoring', '0015_auto_20170214_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weop',
            name='obs_time',
            field=models.TimeField(default=datetime.datetime(2017, 2, 14, 11, 8, 26, 120000)),
        ),
    ]
