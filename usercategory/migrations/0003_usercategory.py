# Generated by Django 4.1.5 on 2023-02-17 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usercategory', '0002_alter_beneficiarymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ADMIN', 'System Admin'), ('BENEFICIARY', 'Beneficiary User Category'), ('EMPLOYER', 'Employer User Category'), ('OFFICER', 'Loan Officer User Category')], default='BENEFICIARY', max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('beneficiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='beneficiary', to='usercategory.beneficiarymodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('UserCategory',),
                'verbose_name_plural': 'UserCategories',
                'db_table': 'tbl_user_mgt_user_categories',
            },
        ),
    ]
