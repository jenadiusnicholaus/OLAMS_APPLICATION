# Generated by Django 4.1.5 on 2023-02-28 09:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('applicantProfile', '0001_initial'),
        ('education_info', '0003_delete_tbldiplomadetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblDiplomaDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('app_year', models.CharField(max_length=4, null=True)),
                ('avn', models.CharField(max_length=60, null=True)),
                ('entryYear', models.CharField(max_length=10, null=True)),
                ('graduateYear', models.CharField(max_length=10, null=True)),
                ('gpa', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, null=True)),
                ('registrationNumber', models.CharField(max_length=60, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ed_diploma_info_tbl_app_applicant', to='applicantProfile.tblappprofile')),
                ('diplomaInstitution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_diploma_institution', to='education_info.tbldiplomainstitutions')),
            ],
            options={
                'verbose_name': '9:TBL Eduction Diploma infos ',
                'verbose_name_plural': '9:TBL Eduction Diploma infos ',
                'db_table': 'tbl_application_diploma_details',
                'ordering': ['-created_at'],
            },
        ),
    ]
