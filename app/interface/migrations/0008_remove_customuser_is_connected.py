# Generated by Django 4.1.5 on 2023-01-19 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("interface", "0007_customuser_chat_id_customuser_is_connected"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="is_connected",
        ),
    ]
