# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loss_db', '0002_auto_20181105_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damagetypevalue',
            name='sendai_indicator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loss_db.SendaiIndicator'),
        ),
    ]
