# Generated by Django 4.2.11 on 2024-03-21 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sitesx", "0002_zone_lead"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="site",
            name="ip_address",
        ),
        migrations.RemoveField(
            model_name="site",
            name="username",
        ),
        migrations.CreateModel(
            name="Instance",
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
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField(blank=True)),
                (
                    "ip_address",
                    models.CharField(
                        blank=True,
                        help_text="IPv4 address for the instance",
                        max_length=16,
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True, help_text="Username for ssh access", max_length=50
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sitesx.site"
                    ),
                ),
            ],
        ),
    ]
