# Generated by Django 4.1.5 on 2023-02-19 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demographics', '0002_tbldemographicsdetails'),
        ('guarantordetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_guarantordetailslug',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_district', to='demographics.tblregions'),
        ),
        migrations.AddField(
            model_name='tbl_guarantordetailslug',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_region_lug', to='demographics.tblregions'),
        ),
        migrations.AddField(
            model_name='tbl_guarantordetailspgd',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_district_pgd', to='demographics.tbldistrict'),
        ),
        migrations.AddField(
            model_name='tbl_guarantordetailspgd',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantor_region_pgd', to='demographics.tblregions'),
        ),
    ]