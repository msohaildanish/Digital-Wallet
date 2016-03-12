# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0020_auto_20160129_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='expiry_time_of_credited_amount',
            field=models.DateTimeField(default=datetime.datetime(2030, 1, 1, 0, 0), blank=True),
        ),
    ]
