# Generated by Django 4.1.5 on 2023-02-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0046_alter_tbl_app_nonenectadetails_original_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_app_applicant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_app_applicantdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_app_applicanttype',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_app_categories',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_app_nectadetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_app_nonenectadetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_app_paymentdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_app_profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
