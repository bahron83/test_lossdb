# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss_db', '0008_auto_20181106_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventattributevaluevarchar',
            name='data_type',
            field=models.CharField(choices=[(b'varchar', b'varchar')], default='varchar', max_length=25),
            preserve_default=False,
        ),
    ]
