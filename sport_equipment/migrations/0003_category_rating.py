# Generated by Django 4.1.4 on 2022-12-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sport_equipment", "0002_debugequipment"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="rating",
            field=models.PositiveIntegerField(default=0),
        ),
    ]