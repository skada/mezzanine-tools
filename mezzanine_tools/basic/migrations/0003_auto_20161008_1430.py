# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CategoryPage',
        ),
    ]
