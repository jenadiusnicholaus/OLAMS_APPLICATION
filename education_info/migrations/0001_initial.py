# Generated by Django 4.1.5 on 2023-02-17 10:13

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
            name='TBL_Education_institution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('institute_type', models.CharField(choices=[('DIPLOMA', 'DIPLOMA'), ('HIGH_LEVEL_EDUCATION', 'HIGH LEVEL EDUCTION')], max_length=20, null=True)),
                ('institute_name', models.CharField(max_length=60, null=True)),
                ('instituteCode', models.CharField(max_length=35, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '7: TBL Eduction Institute',
                'verbose_name_plural': '7: TBL Eduction Institute',
                'db_table': 'tbl_diploma_institutions',
            },
        ),
        migrations.CreateModel(
            name='TBL_Education_TertiaryEducationInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('admittedDegreeCategory', models.CharField(default='Master', max_length=15)),
                ('applicationYear', models.IntegerField(default='2023')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '6:TBL Tertiary Education infos',
                'verbose_name_plural': '6:TBL Tertiary Education infos',
                'db_table': 'tbl_tertiary_education',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TblCourses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=50)),
                ('courseCode', models.CharField(max_length=30)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '8. TBL_COURSES',
                'verbose_name_plural': '8. TBL_COURSES',
                'db_table': 'tbl_courses',
            },
        ),
        migrations.CreateModel(
            name='TblTertiaryEducationAwards',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('award', models.CharField(max_length=50)),
                ('regno', models.CharField(max_length=40)),
                ('entryYear', models.IntegerField()),
                ('graduateYear', models.IntegerField()),
                ('awardCategory', models.CharField(max_length=20)),
                ('gpa', models.FloatField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='TblAwardsInstitution', to='education_info.tbl_education_institution')),
                ('tertiaryInfo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='TblAwards_TertiaryInfo', to='education_info.tbl_education_tertiaryeducationinfos')),
            ],
            options={
                'verbose_name': '9. Tertiary Education Award',
                'verbose_name_plural': '9. Tertiary Education Award',
                'db_table': 'tbl_tertiary_education_awards',
            },
        ),
        migrations.CreateModel(
            name='TblInstitutionCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='education_info.tblcourses')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='education_info.tbl_education_institution')),
            ],
            options={
                'verbose_name': '10: Institution Course',
                'verbose_name_plural': '10: Institution Course',
                'db_table': 'tbl_institutioncourses',
            },
        ),
        migrations.CreateModel(
            name='TBL_EducationInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('f4_no_of_seat', models.IntegerField(default=0)),
                ('pst4ed', models.CharField(max_length=30, null=True)),
                ('f4sps', models.CharField(max_length=30, null=True)),
                ('f4sps_cp', models.CharField(max_length=30, null=True)),
                ('f4sps_cp_phone', models.CharField(max_length=30, null=True)),
                ('f4sps_cp_addr', models.CharField(max_length=30, null=True)),
                ('pst4sps', models.CharField(max_length=30, null=True)),
                ('pst4sps_cp', models.CharField(max_length=30, null=True)),
                ('pst4sps_cp_phone', models.CharField(max_length=30, null=True)),
                ('pst4sps_cp_addr', models.CharField(max_length=30, null=True)),
                ('ay', models.CharField(max_length=30, null=True)),
                ('confirm', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_tbl_app_applicant', to='loans_application.tbl_app_applicant')),
            ],
            options={
                'verbose_name': '1: TBL Education',
                'verbose_name_plural': '1: TBL Education',
                'db_table': 'tbl_application_education_info',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='tbl_education_tertiaryeducationinfos',
            name='admittedCourse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='education_info.tblcourses'),
        ),
        migrations.AddField(
            model_name='tbl_education_tertiaryeducationinfos',
            name='admittedInstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='education_info.tbl_education_institution'),
        ),
        migrations.AddField(
            model_name='tbl_education_tertiaryeducationinfos',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_te_info_tbl_app_applicant', to='loans_application.tbl_app_applicant'),
        ),
        migrations.CreateModel(
            name='TBL_Education_FormSixInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('index_no', models.CharField(max_length=16)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_form6_info_tbl_app_applicant', to='loans_application.tbl_app_applicant')),
            ],
            options={
                'verbose_name': '4:TBL Eduction Form Six infos ',
                'verbose_name_plural': '4:TBL Eduction Form Six infos ',
                'db_table': 'tbl_application_form_six_details',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TBL_Education_FormFourInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('index_no', models.CharField(max_length=16)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_form4_info_tbl_app_applicant', to='loans_application.tbl_app_applicant')),
            ],
            options={
                'verbose_name': '3: TBL Eduction Form four infos ',
                'verbose_name_plural': '3: TBL Eduction Form four infos ',
                'db_table': 'tbl_application_form_four_details',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TBL_Education_DiplomaInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_diploma_info_tbl_app_applicant', to='loans_application.tbl_app_applicant')),
            ],
            options={
                'verbose_name': '5:TBL Eduction Diploma infos ',
                'verbose_name_plural': '5:TBL Eduction Diploma infos ',
                'db_table': 'tbl_application_diploma_details',
                'ordering': ['-created_at'],
            },
        ),
    ]
