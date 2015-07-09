# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_broadcast_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='details',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='new',
            name='picture',
            field=models.URLField(max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
