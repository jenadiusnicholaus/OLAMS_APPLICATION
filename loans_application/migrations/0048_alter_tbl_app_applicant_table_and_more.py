# Generated by Django 4.1.5 on 2023-02-17 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0047_alter_tbl_app_applicant_id_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tbl_app_applicant',
            table='tbl_applicants',
        ),
        migrations.AlterModelTable(
            name='tbl_app_applicantdetails',
            table='tbl_applicants_details',
        ),
        migrations.AlterModelTable(
            name='tbl_app_applicanttype',
            table='tbl_application_type',
        ),
        migrations.AlterModelTable(
            name='tbl_app_categories',
            table='tbl_applicant_category',
        ),
        migrations.AlterModelTable(
            name='tbl_app_nectadetails',
            table='tbl_necta_details',
        ),
        migrations.AlterModelTable(
            name='tbl_app_nonenectadetails',
            table='tbl_non_necta_details',
        ),
        migrations.AlterModelTable(
            name='tbl_app_paymentdetails',
            table='tbl_application_payment_details',
        ),
        migrations.AlterModelTable(
            name='tbl_app_profile',
            table='tbl_applicant_profile',
        ),
    ]
