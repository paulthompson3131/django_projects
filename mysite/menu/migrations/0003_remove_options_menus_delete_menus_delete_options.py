# Generated by Django 4.2.7 on 2024-12-17 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_rename_menu_menus_rename_menu_options_menus"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="options",
            name="menus",
        ),
        migrations.DeleteModel(
            name="Menus",
        ),
        migrations.DeleteModel(
            name="Options",
        ),
    ]
