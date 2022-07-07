# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 11:05


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("repository", "0013_auto_20170314_1055"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="list_as_author",
        ),
        migrations.AddField(
            model_name="person",
            name="list_in_people",
            field=models.BooleanField(
                default=False,
                help_text=b"Should this person be included in the list of people?",
            ),
            preserve_default=False,
        ),
    ]
