# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-28 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlemaps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='googlemap',
            name='map_before_text',
            field=models.BooleanField(default=False, verbose_name='Map before text'),
        ),
    ]
