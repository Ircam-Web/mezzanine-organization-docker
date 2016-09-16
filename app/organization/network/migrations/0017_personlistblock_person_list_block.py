# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-16 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0016_auto_20160916_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='personlistblock',
            name='person_list_block',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='organization-network.PersonListBlock'),
            preserve_default=False,
        ),
    ]
