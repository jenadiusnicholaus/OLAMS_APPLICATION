# Generated by Django 4.1.5 on 2023-02-20 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicantProfile', '0001_initial'),
        ('guarantordetails', '0003_alter_tbl_guarantordetailslug_applicant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_guarantordetailslug',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guarantor_tbl_app_applicant', to='applicantProfile.tbl_app_profile'),
        ),
        migrations.AlterField(
            model_name='tbl_guarantordetailspgd',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guarantor_PGD_tbl_app_applicant', to='applicantProfile.tbl_app_profile'),
        ),
    ]