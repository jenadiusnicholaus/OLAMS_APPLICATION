from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from loans_application.models import *


# Create your models here.
class TblPreliminaryInfo(models.Model):
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete=models.DO_NOTHING, null=True,
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


class TblParentsInfo(models.Model):
    preliminary = models.ForeignKey(TblPreliminaryInfo, on_delete=models.DO_NOTHING,
                                    related_name="tbl_parent_preliminary")
    firstName = models.CharField(max_length=40, null=False)
    middleName = models.CharField(max_length=40, null=False)
    lastName = models.CharField(max_length=40, null=False)
    occupation = models.CharField(null=False, max_length=50)
    postalAddress = models.CharField(max_length=50)
    physicalAddress = models.CharField(max_length=50, null=False)
    mobileNumber = PhoneNumberField(null=False)
    gender = models.CharField(max_length=1, null=False)
    applicantRelationship = models.CharField(null=False, max_length=20)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


class TblParentDeathInfo(models.Model):
    preliminary = models.ForeignKey(TblPreliminaryInfo, on_delete=models.DO_NOTHING,
                                    related_name="tbl_parentsDeathInfo_preliminary")
    deathCertificateNo = models.CharField(max_length=40, null=False)
    deceasedName = models.CharField(null=False, max_length=60)
    applicantRelationship = models.CharField(null=False, max_length=20)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


class TblDisability(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "4: TBL Disability"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TblDisabilityInfo(models.Model):
    preliminary = models.ForeignKey(TblPreliminaryInfo, on_delete=models.DO_NOTHING, null=False,
                                    related_name="tbl_disabilityInfo_preliminary")
    disabilityType = models.ForeignKey(TblDisability, on_delete=models.DO_NOTHING, null=False,
                                       related_name="tbl_disabilityInfo_disability")
    disabledPerson = models.CharField(null=False, max_length=20)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


class TblTasafInfo(models.Model):
    preliminary = models.ForeignKey(TblPreliminaryInfo, on_delete=models.DO_NOTHING,
                                    related_name="tbl_tasaf_preliminary")
    firstName = models.CharField(null=False, max_length=40)
    middleName = models.CharField(null=False, max_length=40)
    lastName = models.CharField(null=False, max_length=40)
    dateOfBirth = models.DateField(null=False)
    registrationNo = models.CharField(null=False, max_length=30)
    memberLineNo = models.IntegerField(null=False)
    gender = models.CharField(max_length=10, null=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


class TblOtherFormFourNumber(models.Model):
    preliminary = models.ForeignKey(TblPreliminaryInfo, on_delete=models.DO_NOTHING,
                                    related_name="tbl_otherform4Indexn_preliminary")
    otherFormFourIndexNo = models.CharField(max_length=16, null=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
