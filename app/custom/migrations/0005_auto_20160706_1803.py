# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0004_auto_20160705_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpage',
            name='sub_title',
            field=models.TextField(blank=True, max_length=1000, verbose_name='sub title'),
        ),
        migrations.AlterField(
            model_name='basicpage',
            name='sub_title_en',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='sub title'),
        ),
        migrations.AlterField(
            model_name='basicpage',
            name='sub_title_fr',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='sub title'),
        ),
    ]
