# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockbook', '0002_auto_20150507_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holding',
            name='CP_date',
            field=models.DateField(verbose_name=b'buy date', blank=True),
        ),
        migrations.AlterField(
            model_name='holding',
            name='SP_date',
            field=models.DateField(verbose_name=b'sell date', blank=True),
        ),
        migrations.AlterField(
            model_name='holding',
            name='SP_price',
            field=models.IntegerField(blank=True),
        ),
    ]
