# Generated by Django 4.1.5 on 2023-02-17 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preliminary_info', '0006_alter_tbldisability_id_alter_tbldisabilityinfo_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbldisabilityinfo',
            options={'verbose_name': 'tbl disability details', 'verbose_name_plural': 'tbl disability details'},
        ),
        migrations.AlterModelOptions(
            name='tblotherformfournumber',
            options={'verbose_name': 'tbl other Form four Numbers', 'verbose_name_plural': 'tbl other Form four Numbers'},
        ),
        migrations.AlterModelOptions(
            name='tblparentdeathinfo',
            options={'verbose_name': 'tbl Parent Death Details', 'verbose_name_plural': 'tbl Parent Death Details'},
        ),
        migrations.AlterModelOptions(
            name='tblparentsinfo',
            options={'verbose_name': 'tbl Parents details', 'verbose_name_plural': 'tbl Parents details'},
        ),
        migrations.AlterModelOptions(
            name='tblpreliminaryinfo',
            options={'verbose_name': 'Tbl preliminary info', 'verbose_name_plural': 'Tbl preliminary info'},
        ),
        migrations.AlterModelOptions(
            name='tbltasafinfo',
            options={'verbose_name': 'Tbl tasaf details', 'verbose_name_plural': 'Tbl tasaf details'},
        ),
        migrations.AlterModelTable(
            name='tbldisability',
            table='tbl_disability',
        ),
        migrations.AlterModelTable(
            name='tbldisabilityinfo',
            table='tbl_disability_details',
        ),
        migrations.AlterModelTable(
            name='tblotherformfournumber',
            table='tbl_other_form_four_index_numbers',
        ),
        migrations.AlterModelTable(
            name='tblparentdeathinfo',
            table='tbl_parent_death_details',
        ),
        migrations.AlterModelTable(
            name='tblparentsinfo',
            table='tbl_parents_details',
        ),
        migrations.AlterModelTable(
            name='tblpreliminaryinfo',
            table='tbl_preliminary_info',
        ),
        migrations.AlterModelTable(
            name='tbltasafinfo',
            table='tbl_tasaf_details',
        ),
    ]