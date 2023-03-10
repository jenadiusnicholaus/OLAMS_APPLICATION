# Generated by Django 4.1.5 on 2023-01-27 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans_application', '0033_alter_tbl_app_paymentdetails_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_app_nectadetails',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='tbl_app_nectadetails',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='tbl_app_nonenectadetails',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='tbl_app_nonenectadetails',
            name='last_name',
        ),
        migrations.AddField(
            model_name='tbl_app_nectadetails',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='necta_applicant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tbl_app_nonenectadetails',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='none_necta_applicant', to=settings.AUTH_USER_MODEL),
        ),
    ]
