# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 18:57
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lookup_tables', '0006_auto_20170215_0857'),
        ('downed_wildlife_monitoring', '0018_auto_20170214_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEEFReporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trial_date', models.DateField(default=django.utils.timezone.now)),
                ('loc', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('notes', models.TextField(blank=True, null=True)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.SpeciesDef')),
                ('turbine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.Infrastructure')),
            ],
        ),
        migrations.AddField(
            model_name='seefmaster',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weop',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caremonitoring',
            name='monitor_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='caremonitoring',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caresetup',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='photo_as_found',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='photo_as_found2',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='photo_injury',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='photo_other',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='photo_structure',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='time_collected',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='time_reported',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='downedwildlifemonitoring',
            name='time_responded',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kwpiisearching',
            name='monitor_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='kwpiisearching',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kwpisearching',
            name='monitor_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='kwpisearching',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nenesurvey',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wacardswap',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wacardswap',
            name='swap_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='weop',
            name='obs_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
