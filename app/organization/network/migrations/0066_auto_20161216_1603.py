# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-16 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0065_auto_20161208_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('name_fr', models.CharField(max_length=512, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=512, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('description_fr', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='description')),
                ('url', models.URLField(blank=True, max_length=512, verbose_name='URL')),
                ('image', mezzanine.core.fields.FileField(max_length=1024, verbose_name='Image')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='bio',
            field=models.TextField(blank=True, verbose_name='bio'),
        ),
        migrations.AddField(
            model_name='organization',
            name='bio_en',
            field=models.TextField(blank=True, null=True, verbose_name='bio'),
        ),
        migrations.AddField(
            model_name='organization',
            name='bio_fr',
            field=models.TextField(blank=True, null=True, verbose_name='bio'),
        ),
        migrations.AddField(
            model_name='organizationservice',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='organization-network.Organization', verbose_name='organization'),
        ),
    ]