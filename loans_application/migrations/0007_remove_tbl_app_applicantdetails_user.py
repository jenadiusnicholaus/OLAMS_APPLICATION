# Generated by Django 4.1.5 on 2023-01-18 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "loans_application",
            "0006_remove_tbl_app_initialapplicantcategory_name_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tbl_app_applicantdetails",
            name="user",
        ),
    ]
