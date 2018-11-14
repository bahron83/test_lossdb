# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss_db', '0010_auto_20181106_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='damageassessmentvalue',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='damageassessmentvalue',
            name='lon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eventattributevaluedate',
            name='data_type',
            field=models.CharField(default=b'date', max_length=25),
        ),
        migrations.AlterField(
            model_name='eventattributevaluedecimal',
            name='data_type',
            field=models.CharField(default=b'decimal', max_length=25),
        ),
        migrations.AlterField(
            model_name='eventattributevalueint',
            name='data_type',
            field=models.CharField(default=b'int', max_length=25),
        ),
        migrations.AlterField(
            model_name='eventattributevaluetext',
            name='data_type',
            field=models.CharField(default=b'text', max_length=25),
        ),
    ]
