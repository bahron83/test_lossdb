# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss_db', '0004_auto_20181106_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='entity_type',
            field=models.CharField(choices=[(b'asset', b'asset'), (b'event', b'event')], max_length=25),
        ),
        migrations.AlterField(
            model_name='eavattribute',
            name='entity_type',
            field=models.CharField(choices=[(b'asset', b'asset'), (b'event', b'event')], max_length=25),
        ),
        migrations.AlterField(
            model_name='event',
            name='entity_type',
            field=models.CharField(choices=[(b'asset', b'asset'), (b'event', b'event')], max_length=25),
        ),
        migrations.DeleteModel(
            name='EntityType',
        ),
    ]
