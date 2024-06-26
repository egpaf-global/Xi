# Generated by Django 4.2.11 on 2024-03-19 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sitesx", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="zone",
            name="lead",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_lead",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
