# Generated by Django 4.1.5 on 2023-03-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education_info', '0005_alter_tbldiplomadetails_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblsponsordetails',
            name='app_year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
