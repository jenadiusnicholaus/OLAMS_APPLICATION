

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0048_alter_tbl_app_applicant_table_and_more'),
        ('education_info', '0002_tbl_education_applicantattendedschool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_education_diplomainfos',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_diploma_info_tbl_app_applicant', to='loans_application.tbl_app_profile'),
        ),
        migrations.AlterField(
            model_name='tbl_education_formfourinfos',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_form4_info_tbl_app_applicant', to='loans_application.tbl_app_profile'),
        ),
        migrations.AlterField(
            model_name='tbl_education_formsixinfos',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_form6_info_tbl_app_applicant', to='loans_application.tbl_app_profile'),
        ),
        migrations.AlterField(
            model_name='tbl_education_tertiaryeducationinfos',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_te_info_tbl_app_applicant', to='loans_application.tbl_app_profile'),
        ),
        migrations.AlterField(
            model_name='tbl_educationinfo',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ed_tbl_app_applicant', to='loans_application.tbl_app_profile'),
        ),
    ]
