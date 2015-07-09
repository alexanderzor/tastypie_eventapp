# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20150530_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcast',
            name='online_date',
        ),
    ]
