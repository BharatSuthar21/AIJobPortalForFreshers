# Generated by Django 5.0.1 on 2024-10-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "userId",
                    models.IntegerField(
                        default=1111, primary_key=True, serialize=False
                    ),
                ),
                ("joiningDate", models.DateTimeField(auto_now_add=True)),
                ("userType", models.BooleanField(default=False)),
            ],
        ),
    ]
