# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 20:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downed_wildlife_monitoring', '0006_auto_20170209_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weop',
            name='obs_time',
            field=models.TimeField(default=datetime.datetime(2017, 2, 9, 10, 35, 20, 426351)),
        ),
    ]
