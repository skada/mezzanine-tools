# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, editable=False, verbose_name='Created')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('validated', models.BooleanField(default=False, verbose_name='Validated')),
                ('code', models.UUIDField(db_index=True, unique=True, verbose_name='Code')),
                ('site', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletter',
            },
        ),
    ]