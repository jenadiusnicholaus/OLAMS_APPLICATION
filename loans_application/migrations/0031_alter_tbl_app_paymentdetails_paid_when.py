# Generated by Django 4.1.5 on 2023-01-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0030_alter_tbl_app_applicant_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_app_paymentdetails',
            name='paid_when',
            field=models.DateTimeField(null=True),
        ),
    ]
