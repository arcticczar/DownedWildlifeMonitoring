# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 22:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downed_wildlife_monitoring', '0016_auto_20170214_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weop',
            name='obs_time',
            field=models.TimeField(default=datetime.datetime(2017, 2, 14, 12, 40, 20, 884000)),
        ),
    ]
