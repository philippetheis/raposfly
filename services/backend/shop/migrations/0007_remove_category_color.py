# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20161121_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='color',
        ),
    ]
