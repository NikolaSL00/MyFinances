# Generated by Django 5.0.1 on 2024-02-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0017_featureflags"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("DEV", "Developer"),
                    ("STAFF", "Staff"),
                    ("USER", "User"),
                    ("TESTER", "Tester"),
                ],
                default="USER",
                max_length=10,
            ),
        ),
    ]
