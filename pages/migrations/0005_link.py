# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-25 07:30


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_page_nav_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=200)),
                ("url", models.URLField()),
                ("order", models.IntegerField(default=-1)),
            ],
        ),
    ]
