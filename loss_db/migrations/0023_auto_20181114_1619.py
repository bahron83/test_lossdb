# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loss_db', '0022_auto_20181113_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetAttributeValueDate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_type', models.CharField(default=b'date', max_length=25)),
                ('value', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetAttributeValueDecimal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_type', models.CharField(default=b'decimal', max_length=25)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetAttributeValueInt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_type', models.CharField(default=b'int', max_length=25)),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetAttributeValueText',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_type', models.CharField(default=b'text', max_length=25)),
                ('value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetAttributeValueVarchar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_type', models.CharField(default=b'varchar', max_length=25)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='asset',
            name='entity_type',
        ),
        migrations.RemoveField(
            model_name='event',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='event',
            name='entity_type',
        ),
        migrations.AddField(
            model_name='damageassessment',
            name='damage_types',
            field=models.ManyToManyField(through='loss_db.DamageTypeValue', to='loss_db.DamageType'),
        ),
        migrations.AddField(
            model_name='damageassessment',
            name='items',
            field=models.ManyToManyField(related_name='assessment_for_item', through='loss_db.DamageAssessmentValue', to='loss_db.AssetItem'),
        ),
        migrations.AddField(
            model_name='damageassessment',
            name='phenomena',
            field=models.ManyToManyField(related_name='assessment_for_phenomenon', through='loss_db.DamageAssessmentValue', to='loss_db.Phenomenon'),
        ),
        migrations.AddField(
            model_name='assetattributevaluevarchar',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.Asset'),
        ),
        migrations.AddField(
            model_name='assetattributevaluevarchar',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.EavAttribute'),
        ),
        migrations.AddField(
            model_name='assetattributevaluetext',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.Asset'),
        ),
        migrations.AddField(
            model_name='assetattributevaluetext',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.EavAttribute'),
        ),
        migrations.AddField(
            model_name='assetattributevalueint',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.Asset'),
        ),
        migrations.AddField(
            model_name='assetattributevalueint',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.EavAttribute'),
        ),
        migrations.AddField(
            model_name='assetattributevaluedecimal',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.Asset'),
        ),
        migrations.AddField(
            model_name='assetattributevaluedecimal',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.EavAttribute'),
        ),
        migrations.AddField(
            model_name='assetattributevaluedate',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.Asset'),
        ),
        migrations.AddField(
            model_name='assetattributevaluedate',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_db.EavAttribute'),
        ),
    ]
