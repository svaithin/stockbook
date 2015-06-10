# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockbook', '0005_auto_20150513_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='holding',
            name='Qty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
