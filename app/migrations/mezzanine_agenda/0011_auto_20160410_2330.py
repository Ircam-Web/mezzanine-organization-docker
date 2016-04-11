# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0010_eventlocation_external_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventprice',
            name='price',
        ),
        migrations.AddField(
            model_name='eventprice',
            name='value',
            field=models.FloatField(default=0, verbose_name='value'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='featured_name',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='featured name'),
        ),
    ]