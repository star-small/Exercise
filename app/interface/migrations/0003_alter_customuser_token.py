# Generated by Django 4.1.5 on 2023-01-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interface", "0002_alter_customuser_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="token",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
