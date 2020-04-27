# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-05 14:22


import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0023_auto_20170705_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['slug']},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='x', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taggroup',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='x', editable=True, populate_from=b'name', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taggroup',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
