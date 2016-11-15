# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-13 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0059_auto_20161113_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='opening_times_en',
            field=models.TextField(blank=True, null=True, verbose_name='opening times'),
        ),
        migrations.AddField(
            model_name='organization',
            name='opening_times_fr',
            field=models.TextField(blank=True, null=True, verbose_name='opening times'),
        ),
        migrations.AddField(
            model_name='organization',
            name='subway_access_en',
            field=models.TextField(blank=True, null=True, verbose_name='subway access'),
        ),
        migrations.AddField(
            model_name='organization',
            name='subway_access_fr',
            field=models.TextField(blank=True, null=True, verbose_name='subway access'),
        ),
    ]