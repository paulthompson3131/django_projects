# Generated by Django 4.2.7 on 2025-01-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0007_remove_menucontent_form_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="menucontent",
            name="back_url",
            field=models.CharField(default="menu", max_length=128),
        ),
    ]
