# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CP_date', models.DateTimeField(verbose_name=b'date published')),
                ('SP_date', models.DateField(verbose_name=b'date published')),
                ('CP_price', models.IntegerField()),
                ('SP_price', models.IntegerField()),
                ('Customer', models.ForeignKey(to='stockbook.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Stk_id', models.CharField(max_length=10)),
                ('Stk_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='holding',
            name='Stock_id',
            field=models.ForeignKey(to='stockbook.Stocks'),
        ),
    ]
