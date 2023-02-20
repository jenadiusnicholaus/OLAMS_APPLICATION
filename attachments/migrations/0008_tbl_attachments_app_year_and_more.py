# Generated by Django 4.1.5 on 2023-02-19 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicantProfile', '0001_initial'),
        ('attachments', '0007_alter_tbl_attachments_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_attachments',
            name='app_year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_attachments',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='attachment_tbl_app_applicant', to='applicantProfile.tbl_app_profile'),
        ),
    ]