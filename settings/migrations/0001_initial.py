# Generated by Django 4.1.5 on 2023-02-17 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OlamsConfigurations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('configurationName', models.CharField(max_length=100, unique=True)),
                ('configurationValue', models.CharField(max_length=260)),
                ('createdBy', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Olams Configurations',
                'verbose_name_plural': 'Olams Configurations',
                'db_table': 'tbl_olams_configurations',
            },
        ),
    ]
