# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20150601_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcast',
            name='description',
        ),
        migrations.RemoveField(
            model_name='broadcast',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='new',
            name='picture',
        ),
    ]
