# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-16 10:13


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("repository", "0045_auto_20190816_1110"),
    ]

    operations = [
        migrations.AddField(
            model_name="researchitem",
            name="generate_thumbnail",
            field=models.CharField(
                blank=True,
                choices=[
                    (b"B", b"Blog"),
                    (b"R", b"Report"),
                    (b"P", b"Policy"),
                    (b"C", b"Consultation"),
                    (b"M", b"Blog"),
                ],
                help_text=b"Generate a thumbnail from the hero image",
                max_length=2,
                null=True,
            ),
        ),
    ]
