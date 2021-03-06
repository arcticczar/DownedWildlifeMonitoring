# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BurrowMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitoring_date', models.DateField()),
                ('enclosure', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
                ('burrow_num', models.IntegerField()),
                ('tootpick_activity', models.BooleanField()),
                ('feather_activity', models.BooleanField()),
                ('chick_present', models.BooleanField()),
                ('nest_material_present', models.BooleanField()),
                ('ant_activity', models.BooleanField()),
                ('other_activity', models.BooleanField()),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
    ]
