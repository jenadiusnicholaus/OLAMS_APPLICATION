# Generated by Django 4.1.5 on 2023-01-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loans_application", "0011_tbl_app_nonenectadetails_exam_year_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tbl_app_nectadetails",
            name="last_name",
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name="tbl_app_nonenectadetails",
            name="last_name",
            field=models.CharField(max_length=16, null=True),
        ),
    ]
