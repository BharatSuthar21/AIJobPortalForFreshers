# Generated by Django 5.0.1 on 2024-10-01 14:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyDetails",
            fields=[
                ("companyId", models.AutoField(primary_key=True, serialize=False)),
                ("companyName", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("industryType", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("phoneNumber", models.CharField(blank=True, max_length=20, null=True)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("website", models.URLField(blank=True, max_length=255, null=True)),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="company_logos/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("sector", models.CharField(blank=True, max_length=100, null=True)),
                ("revenue", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "company_size",
                    models.CharField(
                        choices=[
                            ("1-10", "1-10 employees"),
                            ("11-50", "11-50 employees"),
                            ("51-200", "51-200 employees"),
                            ("201-500", "201-500 employees"),
                            ("500+", "500+ employees"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContestDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=1000)),
                ("link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="InternshipDetails",
            fields=[
                ("internshipId", models.AutoField(primary_key=True, serialize=False)),
                ("internshipDescription", models.TextField()),
                ("qualifications", models.TextField()),
                ("payRange", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=255)),
                (
                    "companyId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.companydetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobDetails",
            fields=[
                ("jobId", models.AutoField(primary_key=True, serialize=False)),
                ("jobDescription", models.TextField()),
                ("qualifications", models.TextField()),
                ("payRange", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=255)),
                (
                    "companyId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.companydetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "razor_pay_order_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "razor_pay_payment_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "razor_pay_patment_signature",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("headline", models.CharField(max_length=1000)),
                ("summary", models.CharField(max_length=10000000)),
                ("link", models.URLField()),
                ("percent", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
