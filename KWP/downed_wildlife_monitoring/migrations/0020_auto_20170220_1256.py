# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('downed_wildlife_monitoring', '0019_auto_20170215_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caresetup',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='weather_TOD',
            field=models.CharField(blank=True, default=b'unknown', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nenesurvey',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
