# Generated by Django 4.2.1 on 2023-05-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EDLEntry",
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
                (
                    "entry_type",
                    models.CharField(
                        choices=[("IP", "IP Address"), ("Domain", "Domain Name")],
                        max_length=50,
                    ),
                ),
                ("entry_value", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
