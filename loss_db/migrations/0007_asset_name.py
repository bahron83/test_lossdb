# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss_db', '0006_auto_20181106_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='name',
            field=models.CharField(default='Palazzo Lombardia', max_length=50),
            preserve_default=False,
        ),
    ]
