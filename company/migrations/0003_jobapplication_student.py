# Generated by Django 5.0.1 on 2024-10-05 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0002_remove_companydetails_company_size_and_more"),
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobapplication",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student.studentdetails"
            ),
        ),
    ]
