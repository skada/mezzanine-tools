# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-28 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleForm',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('form_url', models.URLField(verbose_name='Form URL')),
                ('form_width', models.SmallIntegerField(blank=True, null=True, verbose_name='Width')),
                ('form_height', models.SmallIntegerField(blank=True, null=True, verbose_name='Height')),
                ('form_before_text', models.BooleanField(default=False, verbose_name='Map before text')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Google form',
                'verbose_name_plural': 'Google forms',
            },
            bases=('pages.page', models.Model),
        ),
    ]
