# Generated by Django 4.1.5 on 2023-02-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preliminary_info', '0002_alter_tbltasafinfo_memberlineno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblpreliminaryinfo',
            name='formSixOrDiploma',
            field=models.IntegerField(default=1),
        ),
    ]
