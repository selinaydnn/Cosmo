# Generated by Django 4.2.6 on 2024-05-28 20:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_userprofile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
