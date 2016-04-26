# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colecoes', '0004_auto_20160425_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='collection_type',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]