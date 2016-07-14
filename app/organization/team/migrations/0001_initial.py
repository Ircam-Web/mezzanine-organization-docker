# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import mezzanine.core.fields
import mezzanine.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('content_fr', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_en', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('date_begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('role', models.CharField(blank=True, max_length=512, verbose_name='role')),
                ('description', models.TextField(blank=True, verbose_name='work')),
                ('description_fr', models.TextField(blank=True, null=True, verbose_name='work')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='work')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, verbose_name='address')),
                ('postal_code', models.CharField(blank=True, max_length=16, verbose_name='postal code')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('name_fr', models.CharField(max_length=512, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=512, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('description_fr', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='description')),
                ('url', models.URLField(blank=True, max_length=512, verbose_name='URL')),
                ('weaving_css_class', models.CharField(blank=True, max_length=64, verbose_name='weaving CSS class')),
            ],
            options={
                'verbose_name': 'department',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, help_text='Use this field to define a simple identifier that can be used to style the different link types (i.e. assign social media icons to them)', max_length=256, verbose_name='Slug')),
                ('ordering', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ordering')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'organization type',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('_meta_title', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('photo', mezzanine.core.fields.FileField(blank=True, max_length=1024, verbose_name='photo')),
                ('photo_credits', models.CharField(blank=True, max_length=255, null=True, verbose_name='photo credits')),
                ('photo_alignment', models.CharField(blank=True, choices=[('left', 'left'), ('center', 'center'), ('right', 'right')], default='left', max_length=32, verbose_name='photo alignment')),
                ('photo_description', models.TextField(blank=True, verbose_name='photo description')),
                ('photo_card', mezzanine.core.fields.FileField(blank=True, max_length=1024, verbose_name='card photo')),
                ('photo_card_credits', models.CharField(blank=True, max_length=255, null=True, verbose_name='photo card credits')),
                ('photo_slider', mezzanine.core.fields.FileField(blank=True, max_length=1024, verbose_name='slider photo')),
                ('photo_slider_credits', models.CharField(blank=True, max_length=255, null=True, verbose_name='photo slider credits')),
                ('person_title', models.CharField(blank=True, choices=[('Dr', 'Dr'), ('Prof', 'Prof'), ('Prof Dr', 'Prof Dr')], max_length=16, verbose_name='title')),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=16, verbose_name='gender')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='last name')),
                ('birthday', models.DateField(blank=True, verbose_name='birthday')),
                ('bio', mezzanine.core.fields.RichTextField(blank=True, verbose_name='biography')),
                ('bio_fr', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='biography')),
                ('bio_en', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='biography')),
                ('site', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'person',
                'ordering': ['last_name'],
            },
            bases=(mezzanine.utils.models.AdminThumbMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('name_fr', models.CharField(max_length=512, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=512, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('description_fr', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='description')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization-team.Department', verbose_name='department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organization-team.Address')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('description_fr', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='description')),
                ('url', models.URLField(blank=True, max_length=512, verbose_name='URL')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization-team.OrganizationType', verbose_name='organization type')),
            ],
            options={
                'verbose_name': 'organization',
            },
            bases=('organization-team.address', models.Model),
        ),
        migrations.AddField(
            model_name='link',
            name='link_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization-team.LinkType', verbose_name='Link type'),
        ),
        migrations.AddField(
            model_name='link',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization-team.Person', verbose_name='Person'),
        ),
        migrations.AddField(
            model_name='activity',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization-team.Person', verbose_name='person'),
        ),
        migrations.AddField(
            model_name='activity',
            name='teams',
            field=models.ManyToManyField(to='organization-team.Team', verbose_name='teams'),
        ),
        migrations.AddField(
            model_name='person',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization-team.Organization', verbose_name='organization'),
        ),
        migrations.AddField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization-team.Organization', verbose_name='organization'),
        ),
    ]
