# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup_tables', '0012_auto_20170220_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciesdef',
            name='scientific_name',
            field=models.CharField(max_length=200),
        ),
    ]
