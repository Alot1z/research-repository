# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-30 14:49


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_optout'),
    ]

    operations = [
        migrations.AddField(
            model_name='optout',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
