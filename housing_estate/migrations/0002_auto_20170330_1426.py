# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-30 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_estate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='HasAluminiumWindows',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='HasElectricity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='HasGypsum',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='HasTiles',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='HasWater',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='Rented',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='SelfContained',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='VanishedRoom',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hostelroom',
            name='HasAluminiumWindows',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hostelroom',
            name='HasElectricity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hostelroom',
            name='HasGypsum',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hostelroom',
            name='HasTiles',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hostelroom',
            name='HasWater',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hostelroom',
            name='Rented',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hostelroom',
            name='SelfContained',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hostelroom',
            name='VanishedRoom',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='HasAluminiumWindows',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='HasElectricity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='HasGypsum',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='HasTiles',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='HasWater',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='Rented',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='SelfContained',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='VanishedRoom',
            field=models.BooleanField(default=False),
        ),
    ]
