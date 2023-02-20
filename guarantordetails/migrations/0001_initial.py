

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import guarantordetails.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loans_application', '0048_alter_tbl_app_applicant_table_and_more'),

        ('demographics', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(
            name='TBL_GuarantorDetailsPGD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('postaladdress', models.CharField(max_length=100)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('contact_title', models.CharField(max_length=20, null=True)),
                ('inst', models.CharField(max_length=20, null=True)),
                ('contactperson', models.CharField(max_length=20, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('ay', models.CharField(max_length=20, null=True)),
                ('confirm', models.CharField(max_length=10, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_PGD_tbl_app_applicant', to='loans_application.tbl_app_profile')),

                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_district_pgd', to='demographics.tbldistrict')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_region_pgd', to='demographics.tblregions')),

            ],
            options={
                'verbose_name': '2: Tbl Guarantor details PGD',
                'verbose_name_plural': '2: Tbl Guarantor details PGD',
                'db_table': 'tbl_application_guarantor_details_PGD',
            },
        ),
        migrations.CreateModel(
            name='TBL_GuarantorDetailsLUG',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sur_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=10, null=True)),
                ('postaladdress', models.CharField(max_length=10, null=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('email', models.CharField(max_length=10, null=True)),
                ('ward', models.CharField(max_length=10, null=True)),
                ('village', models.CharField(max_length=10, null=True)),
                ('idcardnumber', models.CharField(max_length=10, null=True)),
                ('cardtype', models.CharField(max_length=10, null=True)),
                ('photo', models.FileField(max_length=10, null=True, upload_to=guarantordetails.models.TBL_GuarantorDetailsLUG.image_upload_to)),
                ('photoverified', models.BooleanField(default=False)),
                ('referenceId', models.CharField(max_length=10, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('confirm', models.CharField(max_length=10, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_tbl_app_applicant', to='loans_application.tbl_app_profile')),

                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_district', to='demographics.tblregions')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_region_lug', to='demographics.tblregions')),

            ],
            options={
                'verbose_name': '1: Guarant details LUG',
                'verbose_name_plural': '1: Guarant details LUG',
                'db_table': 'tbl_application_guarantor_details',
                'ordering': ['-created_at'],
            },
        ),
    ]