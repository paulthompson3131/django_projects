# Generated by Django 4.2.7 on 2024-12-22 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0004_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="menucontent",
            old_name="url",
            new_name="url_to_call",
        ),
    ]
