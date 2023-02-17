from django.db import models


class BeneficiaryModel(models.Model):
    loanee_id = models.BigIntegerField(null=True, blank=True, unique=True)
    index_no = models.CharField(null=False, blank=False, primary_key=True, max_length=50, unique=True)
    first_name = models.CharField(null=False, blank=False, max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    sex = models.CharField(null=False, blank=False, max_length=10)
    national_id = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    control_number = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, null=False, blank=False)
    is_loanee = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.first_name} ({self.index_no})'

    class Meta:
        verbose_name = '1: Beneficiary',
        verbose_name_plural = verbose_name
        db_table = 'tbl_beneficiaries'