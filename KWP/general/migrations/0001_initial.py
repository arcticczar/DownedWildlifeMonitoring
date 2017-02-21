# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 22:56
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lookup_tables', '0012_auto_20170220_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrapCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('trap_date', models.DateField(default=django.utils.timezone.now)),
                ('arrival_status', models.CharField(max_length=50)),
                ('arrival_bait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.Bait')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.Site')),
                ('sublocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.Infrastructure')),
            ],
        ),
        migrations.CreateModel(
            name='TrapLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('trap_number', models.PositiveIntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.Site')),
                ('trap_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.TrapType')),
            ],
        ),
        migrations.AddField(
            model_name='trapcheck',
            name='trap_loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.TrapLocation'),
        ),
    ]
