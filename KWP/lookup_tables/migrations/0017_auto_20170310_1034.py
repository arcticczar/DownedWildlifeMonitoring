# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup_tables', '0016_auto_20170221_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='hire_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
