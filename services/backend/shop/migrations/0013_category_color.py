# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 19:59
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20161201_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=colorful.fields.RGBColorField(blank=True, default='#ffffff', null=True),
        ),
    ]
