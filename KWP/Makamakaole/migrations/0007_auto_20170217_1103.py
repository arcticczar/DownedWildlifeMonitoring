# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lookup_tables', '0006_auto_20170215_0857'),
        ('Makamakaole', '0006_auto_20170215_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='NightSurveyObservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation_time', models.TimeField()),
                ('count', models.PositiveIntegerField()),
                ('quadrat', models.PositiveIntegerField()),
                ('elevation', models.CharField(choices=[(b'Above', b'Above'), (b'Below', b'Below'), (b'Same', b'Same')], max_length=20)),
                ('behavior', models.CharField(choices=[(b'transit', b'Transit'), (b'Circling', b'Circling')], max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
                ('flight_direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.Direction')),
                ('parent_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Makamakaole.NightSurvey')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup_tables.SpeciesDef')),
            ],
        ),
        migrations.RenameField(
            model_name='burrowmonitoring',
            old_name='tootpick_activity',
            new_name='toothpick_activity',
        ),
    ]