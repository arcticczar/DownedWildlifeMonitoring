# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downed_wildlife_monitoring', '0017_auto_20170214_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weop',
            name='obs_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
