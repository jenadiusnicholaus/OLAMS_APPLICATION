# Generated by Django 4.1.5 on 2023-02-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeneficiaryModel',
            fields=[
                ('loanee_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('index_no', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('national_id', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('control_number', models.BigIntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
                ('is_loanee', models.BooleanField()),
            ],
            options={
                'verbose_name': ('Beneficiary',),
                'verbose_name_plural': 'Beneficiaries',
                'db_table': 'tbl_beneficiaries',
            },
        ),
    ]
