# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-16 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0067_auto_20161216_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationservice',
            name='box_size',
            field=models.IntegerField(choices=[(3, 3), (6, 6)], default=3, verbose_name='box size'),
        ),
        migrations.AddField(
            model_name='organizationservice',
            name='css_color',
            field=models.CharField(blank=True, choices=[('orange', 'orange'), ('blue', 'blue'), ('green', 'green')], help_text='Determine color on home.', max_length=64, null=True, verbose_name='class color'),
        ),
    ]
