# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 11:28


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0014_auto_20170314_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchoutput',
            name='button_text_value',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
