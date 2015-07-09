# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='picture',
            field=models.URLField(max_length=500, blank=True),
            preserve_default=True,
        ),
    ]
