# Generated by Django 4.1.5 on 2023-01-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loans_application", "0014_tbl_app_applicantattendedschool"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbl_app_applicantattendedschool",
            name="center_number",
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
