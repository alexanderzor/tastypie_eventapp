# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField(null=True, blank=True)),
                ('description', models.CharField(max_length=400, blank=True)),
                ('duration', durationfield.db.models.fields.duration.DurationField()),
                ('online_date', models.DateField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField(blank=True)),
                ('description', models.CharField(max_length=400)),
                ('details', ckeditor.fields.RichTextField(blank=True)),
                ('picture', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
