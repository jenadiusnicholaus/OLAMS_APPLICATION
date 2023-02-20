
# Generated by Django 4.1.5 on 2023-02-19 12:23


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0048_alter_tbl_app_applicant_table_and_more'),
        ('attachments', '0006_alter_tbl_attachemetsdocs_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_attachments',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='attachment_tbl_app_applicant', to='loans_application.tbl_app_profile'),
        ),
    ]
