# Generated by Django 4.1.5 on 2023-01-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_notes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notes", old_name="note_name", new_name="title",
        ),
        migrations.AddField(
            model_name="notes",
            name="description",
            field=models.CharField(default="description", max_length=200),
        ),
    ]