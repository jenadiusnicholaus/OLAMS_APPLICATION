# Generated by Django 4.1.5 on 2023-01-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education_info', '0008_tbl_education_institution'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbl_education_tertiaryeducationinfos',
            options={'ordering': ['-created_at'], 'verbose_name': '6:TBL Eduction Diploma infos', 'verbose_name_plural': '6:TBL Eduction Diploma infos'},
        ),
        migrations.RenameField(
            model_name='tbl_education_institution',
            old_name='institutite_name',
            new_name='institute_name',
        ),
    ]