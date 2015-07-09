# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20150602_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ['-date']},
        ),
    ]
