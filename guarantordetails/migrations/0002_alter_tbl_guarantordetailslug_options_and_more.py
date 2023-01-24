# Generated by Django 4.1.5 on 2023-01-24 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('demographics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guarantordetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbl_guarantordetailslug',
            options={'ordering': ['-created_at'], 'verbose_name': '1: Guarant details LUG', 'verbose_name_plural': '1: Guarant details LUG'},
        ),
        migrations.AlterField(
            model_name='tbl_guarantordetailslug',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_region_lug', to='demographics.tbl_demo_region'),
        ),
        migrations.CreateModel(
            name='TBL_GuarantorDetailsPGD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postaladdress', models.CharField(max_length=100)),
                ('telephone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('contact_title', models.CharField(max_length=20, null=True)),
                ('inst', models.CharField(max_length=20, null=True)),
                ('contactperson', models.CharField(max_length=20, null=True)),
                ('ay', models.CharField(max_length=20, null=True)),
                ('confirm', models.CharField(max_length=10, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_district_pgd', to='demographics.tbl_demo_district')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_region_pgd', to='demographics.tbl_demo_region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_guarantor_details_pgd', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '2: Tbl Guarantor details PGD',
                'verbose_name_plural': '2: Tbl Guarantor details PGD',
            },
        ),
    ]