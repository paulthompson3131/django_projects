# Generated by Django 4.2.7 on 2025-01-10 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0006_menucontent_form_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menucontent",
            name="form_url",
        ),
    ]
