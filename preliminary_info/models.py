from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from loans_application.models import *
from applicantProfile.models import *


# Create your models here.
class TblPreliminaryInfo(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.DO_NOTHING, null=True,
                                  related_name="tbl_preliminary_applicant")
    applicantDisable = models.BooleanField()
    fatherAlive = models.BooleanField(default=1)
    motherAlive = models.BooleanField(default=1)
    resitFormFour = models.IntegerField(default=1, null=False)
    formSixOrDiploma = models.IntegerField(null=False, default=1)
    fatherDisable = models.BooleanField(default=0)
    motherDisable = models.BooleanField(default=0)
    tasafSponsored = models.BooleanField(default=0)
    hasGuardian = models.BooleanField(default=0)
    appYear = models.CharField(max_length=4, null=False)
    confirm = models.BooleanField(default=0)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Tbl preliminary info"
        verbose_name_plural = verbose_name
        db_table = 'tbl_preliminary_info'

    def __str__(self):
        return self.appYear


class TblParentsInfo(models.Model):

    GENDER_CHOICES = (
        ('M', "MALE"),
        ('F', "FEMALE"),
    )

    RELATIONsHIP_CHOICES = (
        ('Father', 'FATHER'),
        ('Mother', 'MOTHER'),
    )

    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.DO_NOTHING, null=True,
                                  related_name="tbl_parent_info_applicant")
    firstName = models.CharField(max_length=40, null=False)
    middleName = models.CharField(max_length=40, null=False)
    lastName = models.CharField(max_length=40, null=False)
    occupation = models.CharField(null=False, max_length=50)
    postalAddress = models.CharField(max_length=50)
    physicalAddress = models.CharField(max_length=50, null=False)
    mobileNumber = PhoneNumberField(null=False)
    gender = models.CharField(
        max_length=6, null=False, choices=GENDER_CHOICES,)
    applicantRelationship = models.CharField(
        null=False, max_length=20, choices=RELATIONsHIP_CHOICES)
    appYear = models.CharField(max_length=4, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "tbl Parents details"
        verbose_name_plural = verbose_name
        db_table = 'tbl_parents_details'

    def __str__(self):
        return self.firstName


class TblParentDeathInfo(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.DO_NOTHING, null=True,
                                  related_name="tbl_parent_death_applicant")
    deathCertificateNo = models.CharField(max_length=40, null=False)
    deceasedName = models.CharField(null=False, max_length=60)
    applicantRelationship = models.CharField(null=False, max_length=20)
    appYear = models.CharField(max_length=4, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "tbl Parent Death Details"
        verbose_name_plural = verbose_name
        db_table = 'tbl_parent_death_details'

    def __str__(self):
        return self.deceasedName


class TblDisability(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "4: TBL Disability"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_disability'

    def __str__(self):
        return self.name


class TblDisabilityInfo(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.DO_NOTHING, null=True,
                                  related_name="tbl_disability_info_applicant")
    disabilityType = models.ForeignKey(TblDisability, on_delete=models.DO_NOTHING, null=False,
                                       related_name="tbl_disabilityInfo_disability")
    disabledPerson = models.CharField(null=False, max_length=20)
    app_year = models.CharField(max_length=4, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "tbl disability details"
        verbose_name_plural = verbose_name
        db_table = 'tbl_disability_details'

    def __str__(self):
        return self.disabilityType + " " + self.disabledPerson


class TblTasafInfo(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.DO_NOTHING, null=True,
                                  related_name="tbl_tasaf_info_applicant")
    firstName = models.CharField(null=False, max_length=40)
    middleName = models.CharField(null=False, max_length=40)
    lastName = models.CharField(null=False, max_length=40)
    dateOfBirth = models.DateField(null=False)
    registrationNo = models.CharField(null=False, max_length=30)
    memberLineNo = models.IntegerField(null=False)
    app_year = models.CharField(max_length=4, null=True)
    gender = models.CharField(max_length=10, null=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Tbl tasaf details"
        verbose_name_plural = verbose_name
        db_table = 'tbl_tasaf_details'

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.registrationNo


# class TblOtherFormFourNumber(models.Model):
#     id = models.AutoField(primary_key=True)
#     preliminary = models.ForeignKey(TblPreliminaryInfo, on_delete=models.DO_NOTHING,
#                                     related_name="TblOtherForm4Number_preliminary")
#     otherFormFourIndexNo = models.CharField(max_length=16, null=False)
#     updated_at = models.DateTimeField(default=timezone.now)
#     created_at = models.DateTimeField(default=timezone.now)
#     class Meta:
#         verbose_name = "tbl other Form four Numbers"
#         verbose_name_plural = verbose_name
#         db_table = 'tbl_other_form_four_index_numbers'
#     def __str__(self):
#         return self.otherFormFourIndexNo + " " + self.preliminary.appYear
