# Generated by Django 4.1.5 on 2023-01-24 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0028_alter_tbl_app_applicant_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TBL_App_ApplicantAttendedSchool',
        ),
    ]
