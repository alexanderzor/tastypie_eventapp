# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150530_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='picture',
            field=models.URLField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
