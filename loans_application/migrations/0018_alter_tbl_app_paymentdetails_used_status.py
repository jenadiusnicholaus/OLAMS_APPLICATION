# Generated by Django 4.1.5 on 2023-01-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "loans_application",
            "0017_remove_tbl_app_applicantdetails_f4_indexno_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbl_app_paymentdetails",
            name="used_status",
            field=models.CharField(
                choices=[("not_used", "No used"), ("used", "used")], max_length=16
            ),
        ),
    ]
