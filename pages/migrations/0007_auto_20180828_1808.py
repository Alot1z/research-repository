# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-28 17:08


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0006_link_new_window"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="social_big_image",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="page",
            name="social_description",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="page",
            name="social_image",
            field=models.ImageField(
                blank=True,
                help_text=b"Image to be used on social shares of the site",
                null=True,
                upload_to=b"social/",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="social_title",
            field=models.CharField(blank=True, default=b"", max_length=200, null=True),
        ),
    ]
