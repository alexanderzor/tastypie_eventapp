# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150530_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='picture',
            field=models.URLField(max_length=60, blank=True),
            preserve_default=True,
        ),
    ]
