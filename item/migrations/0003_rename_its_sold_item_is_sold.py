# Generated by Django 5.1.1 on 2024-09-09 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0002_alter_category_options_item"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="its_sold",
            new_name="is_sold",
        ),
    ]
