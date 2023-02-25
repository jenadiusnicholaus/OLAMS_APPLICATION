# Generated by Django 4.1.5 on 2023-02-23 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicantProfile', '0001_initial'),
        ('preliminary_info', '0003_tbldisabilityinfo_appyear_tblparentdeathinfo_appyear_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbldisabilityinfo',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tbl_disability_info_applicant', to='applicantProfile.tblappprofile'),
        ),
        migrations.AddField(
            model_name='tblparentdeathinfo',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tbl_parent_death_applicant', to='applicantProfile.tblappprofile'),
        ),
        migrations.AddField(
            model_name='tblparentsinfo',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tbl_parent_info_applicant', to='applicantProfile.tblappprofile'),
        ),
        migrations.AddField(
            model_name='tbltasafinfo',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tbl_tasaf_info_applicant', to='applicantProfile.tblappprofile'),
        ),
    ]
