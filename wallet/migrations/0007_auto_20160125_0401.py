# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 04:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_auto_20160123_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='transaction_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 4, 1, 27, 824734)),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet2user_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Wallet'),
        ),
    ]
