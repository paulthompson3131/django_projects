# Generated by Django 4.2.7 on 2025-01-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0005_rename_url_menucontent_url_to_call"),
    ]

    operations = [
        migrations.AddField(
            model_name="menucontent",
            name="form_url",
            field=models.CharField(default="getemployeesurname", max_length=128),
        ),
    ]
