# Generated by Django 4.1.5 on 2023-02-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0035_remove_tbl_app_nectadetails_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_app_paymentdetails',
            name='payment_status',
            field=models.CharField(choices=[(0, 'Not Paid'), (1, 'Paid')], default='no_paid', max_length=20, null=True),
        ),
    ]