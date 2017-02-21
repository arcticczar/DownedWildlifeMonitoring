# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup_tables', '0011_auto_20170220_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bait',
            name='target_species',
        ),
        migrations.RemoveField(
            model_name='traptype',
            name='target_species',
        ),
        migrations.AlterField(
            model_name='age',
            name='age_text',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='bait',
            name='bait_text',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='bandcolor',
            name='color_text',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='canine',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='direction',
            name='direction_text',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='nightsurvey_behavior',
            name='behavior',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='nightsurvey_distance',
            name='distance_range',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='nightsurvey_elevation',
            name='elevation',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='initials',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='plantspecies',
            name='scientific_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='randompoints',
            name='point_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='searcharea',
            name='to_10',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='searcharea',
            name='to_20',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='searcharea',
            name='to_30',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='searcharea',
            name='to_40',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='searcharea',
            name='to_50',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='searcharea',
            name='to_60',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='searcharea',
            name='to_70',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='searcharea',
            name='to_80',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='locations',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='short',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='sizeclass',
            name='size_txt',
            field=models.CharField(max_length=50, unique=True),
        ),

        migrations.AlterField(
            model_name='status',
            name='status_txt',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='traptype',
            name='trap_type_text',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='rain',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]