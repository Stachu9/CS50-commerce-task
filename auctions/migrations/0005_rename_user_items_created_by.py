# Generated by Django 4.2.6 on 2023-11-17 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_alter_items_description_alter_items_photourl"),
    ]

    operations = [
        migrations.RenameField(
            model_name="items",
            old_name="user",
            new_name="created_by",
        ),
    ]