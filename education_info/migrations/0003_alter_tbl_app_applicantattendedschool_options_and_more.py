# Generated by Django 4.1.5 on 2023-01-24 10:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0029_delete_tbl_app_applicantattendedschool'),
        ('education_info', '0002_tbl_app_applicantattendedschool'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbl_app_applicantattendedschool',
            options={'ordering': ['-created_at'], 'verbose_name': '2:TBL Education Applicant Attended Schools', 'verbose_name_plural': '2:TBL Education Applicant Attended Schools'},
        ),
        migrations.AlterField(
            model_name='tbl_educationinfo',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_tbl_app_applicant', to='loans_application.tbl_app_applicant'),
        ),
        migrations.CreateModel(
            name='TBL_TertiaryEducationInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_te_info_tbl_app_applicant', to='loans_application.tbl_app_applicant')),
            ],
            options={
                'verbose_name': '5:TBL Eduction Diploma infos ',
                'verbose_name_plural': '5:TBL Eduction Diploma infos ',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TBL_FormSixInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_no', models.CharField(max_length=16)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_form6_info_tbl_app_applicant', to='loans_application.tbl_app_applicant')),
            ],
            options={
                'verbose_name': '4:TBL Eduction Form Six infos ',
                'verbose_name_plural': '4:TBL Eduction Form Six infos ',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TBL_FormFourInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_no', models.CharField(max_length=16)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_form4_info_tbl_app_applicant', to='loans_application.tbl_app_applicant')),
            ],
            options={
                'verbose_name': '2:TBL Eduction Form four infos ',
                'verbose_name_plural': '2:TBL Eduction Form four infos ',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TBL_DiplomaInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_diploma_info_tbl_app_applicant', to='loans_application.tbl_app_applicant')),
            ],
            options={
                'verbose_name': '5:TBL Eduction Diploma infos ',
                'verbose_name_plural': '5:TBL Eduction Diploma infos ',
                'ordering': ['-created_at'],
            },
        ),
    ]