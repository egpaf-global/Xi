# Generated by Django 4.2.11 on 2024-03-21 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sitesx", "0004_alter_instance_ip_address_alter_instance_username"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Instance",
        ),
    ]
