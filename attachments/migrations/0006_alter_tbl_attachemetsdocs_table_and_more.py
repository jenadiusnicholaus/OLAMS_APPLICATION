# Generated by Django 4.1.5 on 2023-02-16 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0005_alter_tbl_attachments_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tbl_attachemetsdocs',
            table='tbl_application_attachments_docs',
        ),
        migrations.AlterModelTable(
            name='tbl_attachments',
            table='tbl_application_attachments',
        ),
    ]
