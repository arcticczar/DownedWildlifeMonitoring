# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 18:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lookup_tables', '0001_initial'),
        ('Makamakaole', '0004_auto_20170125_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='NightSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('location_coordinates_x', models.DecimalField(decimal_places=10, max_digits=20)),
                ('location_coordinates_y', models.DecimalField(decimal_places=10, max_digits=20)),
                ('sublocation', models.CharField(max_length=100)),
                ('auditory_minutes_surveyed', models.PositiveIntegerField()),
                ('binocular_minutes_surveyed', models.PositiveIntegerField()),
                ('night_vision_minutes_surveyed', models.PositiveIntegerField()),
                ('cloud_cover', models.PositiveIntegerField()),
                ('wind_speed', models.PositiveIntegerField()),
                ('precipitation', models.PositiveIntegerField()),
                ('survey_quality', models.PositiveIntegerField()),
                ('visibility', models.PositiveIntegerField()),
                ('ceiling', models.PositiveIntegerField()),
                ('comments', models.TextField()),
                ('location_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.Site')),
                ('observer1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='lookup_tables.Personnel')),
                ('observer2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='second', to='lookup_tables.Personnel')),
                ('wind_dir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.Direction')),
            ],
        ),
    ]
