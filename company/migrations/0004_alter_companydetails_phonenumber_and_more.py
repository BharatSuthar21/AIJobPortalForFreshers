# Generated by Django 5.0.1 on 2024-10-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0003_jobapplication_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companydetails",
            name="phoneNumber",
            field=models.CharField(default="1234567890", max_length=20),
        ),
        migrations.AlterField(
            model_name="internshipdetails",
            name="stipend",
            field=models.CharField(default="Unpaid", max_length=100),
        ),
        
    ]
