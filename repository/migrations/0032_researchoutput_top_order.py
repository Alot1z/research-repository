# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-25 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0031_auto_20180524_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchoutput',
            name='top_order',
            field=models.IntegerField(default=-1, help_text=b'Order for under image link'),
        ),
    ]
