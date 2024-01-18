# Generated by Django 4.2.7 on 2023-12-26 22:45

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0007_merge_20231222_1106"),
    ]

    operations = [
        migrations.CreateModel(
            name="TrainTrendData",
            fields=[
                (
                    "tt_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("ticker_symbol", models.CharField(default="NaN", max_length=10)),
                ("post_date", models.IntegerField(default=0)),
                (
                    "sentiment",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(2),
                            django.core.validators.MinValueValidator(0),
                        ]
                    ),
                ),
            ],
        ),
    ]
