# Generated by Django 4.2.7 on 2023-11-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contest_delete_car_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
