# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-16 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0015_auto_20160916_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personlistblock',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_list_block', to='organization-network.Person', verbose_name='Person'),
        ),
    ]
