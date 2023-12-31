# Generated by Django 4.1.5 on 2023-02-18 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Savedpasswords",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("domain", models.CharField(blank=True, max_length=200)),
                ("email", models.CharField(blank=True, max_length=200)),
                ("username", models.CharField(blank=True, max_length=200)),
                ("password", models.CharField(blank=True, max_length=200)),
                ("slug", models.SlugField(blank=True, max_length=30)),
                (
                    "of_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
