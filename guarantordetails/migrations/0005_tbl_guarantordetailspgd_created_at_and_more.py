# Generated by Django 4.1.5 on 2023-01-24 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guarantordetails', '0004_alter_tbl_guarantordetailslug_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_guarantordetailspgd',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tbl_guarantordetailspgd',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]