# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import api.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150601_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcast',
            name='date',
        ),
        migrations.AddField(
            model_name='broadcast',
            name='day',
            field=api.models.DayOfTheWeekField(max_length=1, null=True, choices=[(b'1', '\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a'), (b'2', '\u0412\u0442\u043e\u0440\u043d\u0438\u043a'), (b'3', '\u0421\u0440\u0435\u0434\u0430'), (b'4', '\u0427\u0435\u0442\u0432\u0435\u0440\u0433'), (b'5', '\u041f\u044f\u0442\u043d\u0438\u0446\u0430'), (b'6', '\u0421\u0443\u0431\u0431\u043e\u0442\u0430'), (b'7', '\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435')]),
            preserve_default=True,
        ),
    ]
