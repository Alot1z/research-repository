# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0025_auto_20170707_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchitem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='repository.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_groups',
            field=models.ManyToManyField(blank=True, related_name='tags', to='repository.TagGroup'),
        ),
    ]