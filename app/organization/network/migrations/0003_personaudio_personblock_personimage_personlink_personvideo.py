# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization-media', '0001_initial'),
        ('organization-core', '0001_initial'),
        ('organization-network', '0002_auto_20160901_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonAudio',
            fields=[
                ('audio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organization-media.Audio')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audios', to='organization-network.Person', verbose_name='project')),
            ],
            options={
                'abstract': False,
            },
            bases=('organization-media.audio',),
        ),
        migrations.CreateModel(
            name='PersonBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(max_length=1024, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('with_separator', models.BooleanField(default=False)),
                ('background_color', models.CharField(blank=True, choices=[('black', 'black'), ('yellow', 'yellow'), ('red', 'red')], max_length=32, verbose_name='background color')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blocks', to='organization-network.Person', verbose_name='project')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='PersonImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(max_length=1024, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('file', mezzanine.core.fields.FileField(max_length=1024, verbose_name='Image')),
                ('credits', models.CharField(blank=True, max_length=256, null=True, verbose_name='credits')),
                ('type', models.CharField(choices=[('logo', 'logo'), ('slider', 'slider'), ('card', 'card'), ('page_slider', 'page slider')], max_length=64, verbose_name='type')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='organization-network.Person', verbose_name='project')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=512, verbose_name='URL')),
                ('link_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization-core.LinkType', verbose_name='link type')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='links', to='organization-network.Person', verbose_name='project')),
            ],
            options={
                'verbose_name_plural': 'links',
                'verbose_name': 'link',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonVideo',
            fields=[
                ('video_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organization-media.Video')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='organization-network.Person', verbose_name='project')),
            ],
            options={
                'abstract': False,
            },
            bases=('organization-media.video',),
        ),
    ]
