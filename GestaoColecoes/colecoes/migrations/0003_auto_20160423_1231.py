# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 11:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colecoes', '0002_auto_20160325_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection_Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_series', models.CharField(blank=True, max_length=10, null=True)),
                ('item_number', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('collection_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='colecoes.Collection', verbose_name='the related collection')),
            ],
        ),
        migrations.CreateModel(
            name='Collection_Type',
            fields=[
                ('collection_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('status_datetime', models.DateTimeField()),
                ('created_on', models.DateTimeField()),
                ('created_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('status_datetime', models.DateTimeField()),
                ('created_on', models.DateTimeField()),
                ('collection', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='colecoes.Collection', verbose_name='the related collection')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='the related collection owner')),
            ],
        ),
        migrations.CreateModel(
            name='User_Collection_Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('status_datetime', models.DateTimeField()),
                ('created_on', models.DateTimeField()),
                ('collection_item', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='colecoes.Collection_Item', verbose_name='the related collection item')),
                ('user_collection', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='colecoes.User_Collection', verbose_name='the related user collection')),
            ],
        ),
        migrations.RemoveField(
            model_name='collectionitem',
            name='collection_id',
        ),
        migrations.DeleteModel(
            name='CollectionItem',
        ),
        migrations.AddField(
            model_name='collection',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='colecoes.Collection_Type', verbose_name='the related collection type'),
        ),
    ]
