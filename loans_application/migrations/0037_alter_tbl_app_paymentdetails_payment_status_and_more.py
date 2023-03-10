# Generated by Django 4.1.5 on 2023-02-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0036_alter_tbl_app_paymentdetails_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_app_paymentdetails',
            name='payment_status',
            field=models.CharField(choices=[(0, 'Not Paid'), (1, 'Paid')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_app_paymentdetails',
            name='used_status',
            field=models.CharField(blank=True, choices=[(0, 'Not used'), (1, 'Used')], default=0, max_length=16, null=True),
        ),
    ]
