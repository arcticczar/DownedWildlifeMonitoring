# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 19:20
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lookup_tables', '0007_auto_20170217_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='loc',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326),
        ),
    ]
