# Generated by Django 4.1.5 on 2023-02-17 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0048_alter_tbl_app_applicant_table_and_more'),
        ('education_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TBL_Education_ApplicantAttendedSchool',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('center_number', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('center_name', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('necta_applicants', models.ManyToManyField(to='loans_application.tbl_app_nectadetails')),
            ],
            options={
                'verbose_name': '2: TBL Education Applicant Attended Schools',
                'verbose_name_plural': '2: TBL Education Applicant Attended Schools',
                'db_table': 'tbl_application_secondary_schools',
                'ordering': ['-created_at'],
            },
        ),
    ]
