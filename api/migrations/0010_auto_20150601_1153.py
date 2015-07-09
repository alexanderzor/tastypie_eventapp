# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_broadcast_online_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='description',
            field=models.CharField(max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='title',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='new',
            name='description',
            field=models.CharField(max_length=600),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
    ]
