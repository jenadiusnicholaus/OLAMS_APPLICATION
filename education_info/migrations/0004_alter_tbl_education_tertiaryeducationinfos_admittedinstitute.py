# Generated by Django 4.1.5 on 2023-02-21 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education_info', '0003_institutions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_education_tertiaryeducationinfos',
            name='admittedInstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='education_info.institutions'),
        ),
    ]
