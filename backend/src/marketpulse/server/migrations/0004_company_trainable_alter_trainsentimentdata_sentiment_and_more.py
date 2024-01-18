# Generated by Django 4.2.7 on 2023-12-21 21:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0003_merge_20231221_2117"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="trainable",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="trainsentimentdata",
            name="sentiment",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(2),
                    django.core.validators.MinValueValidator(0),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="validsentimentdata",
            name="sentiment",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(2),
                    django.core.validators.MinValueValidator(0),
                ]
            ),
        ),
    ]
