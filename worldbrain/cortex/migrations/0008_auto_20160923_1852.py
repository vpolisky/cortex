# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-23 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cortex', '0007_auto_20160923_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='last_error_message',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='source',
            name='last_time_crawled',
            field=models.DateTimeField(blank=True),
        ),
    ]
