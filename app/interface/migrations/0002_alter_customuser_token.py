# Generated by Django 4.1.5 on 2023-01-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interface", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="token",
            field=models.UUIDField(unique=True),
        ),
    ]