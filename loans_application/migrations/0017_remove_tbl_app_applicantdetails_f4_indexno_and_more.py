# Generated by Django 4.1.5 on 2023-01-19 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("loans_application", "0016_rename_tbl_app_applicantion_tbl_app_applicant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tbl_app_applicantdetails",
            name="f4_indexno",
        ),
        migrations.RemoveField(
            model_name="tbl_app_applicantdetails",
            name="middle_name",
        ),
        migrations.RemoveField(
            model_name="tbl_app_applicantdetails",
            name="sur_name",
        ),
    ]
