# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockbook', '0003_auto_20150513_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holding',
            name='CP_date',
            field=models.DateField(null=True, verbose_name=b'buy date', blank=True),
        ),
        migrations.AlterField(
            model_name='holding',
            name='SP_date',
            field=models.DateField(null=True, verbose_name=b'sell date', blank=True),
        ),
    ]
