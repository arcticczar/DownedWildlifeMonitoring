# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 18:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('downed_wildlife_monitoring', '0005_auto_20170209_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='discovery_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='time_discovered',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='weop',
            name='obs_time',
            field=models.TimeField(default=datetime.datetime(2017, 2, 9, 8, 52, 27, 96803)),
        ),
    ]
