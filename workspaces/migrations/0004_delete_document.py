# Generated by Django 5.1.5 on 2025-01-15 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("workspaces", "0003_document"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Document",
        ),
    ]
