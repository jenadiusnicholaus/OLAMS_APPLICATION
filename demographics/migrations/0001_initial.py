

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('loans_application', '0048_alter_tbl_app_applicant_table_and_more'),

    ]

    operations = [
        migrations.CreateModel(
            name='TblRegions',
            fields=[
                ('region_id', models.IntegerField(default=111, primary_key=True, serialize=False)),
                ('region_name', models.CharField(max_length=100, null=True, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': '2: TBL Demo Region',
                'verbose_name_plural': '2: TBL Demo Region',
                'db_table': 'tbl_regions',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='TblDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=100, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demographics.tblregions')),
            ],
            options={
                'verbose_name': '3: TBL Demo District',
                'verbose_name_plural': '3: TBL Demo District',
                'db_table': 'tbl_districts',
                'ordering': ['-created_date'],
            },
        ),


        migrations.CreateModel(
            name='TblDemographicsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(null=True)),
                ('disability', models.BooleanField(default=False)),
                ('dom_postal', models.CharField(max_length=50, null=True)),
                ('dom_ward', models.CharField(max_length=50, null=True)),
                ('birth_cert_no', models.CharField(max_length=50, null=True)),
                ('cert_type_id', models.CharField(max_length=50, null=True)),
                ('nationalIdNo', models.CharField(max_length=50, null=True)),
                ('birthplace', models.CharField(max_length=50, null=True)),
                ('dom_village', models.CharField(max_length=30, null=True)),
                ('app_year', models.CharField(max_length=4)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('confirm', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='demo_tbl_app_applicant', to='loans_application.tbl_app_profile')),
                ('distric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='demographics.tbldistrict')),
                ('dom_distric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='demo_domestic_distric', to='demographics.tbldistrict')),
                ('dom_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='demo_domestic_region', to='demographics.tblregions')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='demo_tbl_demo_region', to='demographics.tblregions')),
            ],
            options={
                'verbose_name': '1: TBL Demo Democile Details',
                'verbose_name_plural': '1: TBL Demo Democile Details',
                'db_table': 'tbl_application_demographics_details',
                'ordering': ['-created_at'],
            },
        ),

    ]
