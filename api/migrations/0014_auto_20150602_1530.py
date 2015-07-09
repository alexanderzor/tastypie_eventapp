# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_new_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='online_date',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]
