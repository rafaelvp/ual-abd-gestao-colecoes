# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-02 16:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colecoes', '0006_auto_20160425_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sent_date', models.DateTimeField()),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('message_read', models.BooleanField(default=False)),
                ('message_read_date', models.DateTimeField()),
                ('receiver', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='the message receiver')),
                ('sender', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='the message sender')),
            ],
        ),
    ]
