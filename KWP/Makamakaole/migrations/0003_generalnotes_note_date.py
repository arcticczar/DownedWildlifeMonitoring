# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 21:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Makamakaole', '0002_auto_20170125_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalnotes',
            name='note_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
