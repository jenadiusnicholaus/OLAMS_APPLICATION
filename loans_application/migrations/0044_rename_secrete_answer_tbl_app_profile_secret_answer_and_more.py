# Generated by Django 4.1.5 on 2023-02-06 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans_application', '0043_alter_tbl_app_profile_secrete_answer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_app_profile',
            old_name='secrete_answer',
            new_name='secret_answer',
        ),
        migrations.RenameField(
            model_name='tbl_app_profile',
            old_name='secrete_question',
            new_name='secret_question',
        ),
    ]
