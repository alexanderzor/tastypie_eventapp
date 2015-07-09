# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20150601_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='picture',
            field=models.URLField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
