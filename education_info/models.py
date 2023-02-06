from django.db import models
from loans_application.models import *

class TBL_EducationInfo(models.Model):
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete= models.DO_NOTHING, null = True,related_name="ed_tbl_app_applicant")
    f4_no_of_seat = models.IntegerField(default=0)
    pst4ed = models.CharField(max_length=30, null= True)
    pst4ed = models.CharField(max_length=30, null= True)
    f4sps = models.CharField(max_length=30, null= True)
    f4sps_cp =models.CharField(max_length=30, null= True)
    f4sps_cp_phone = models.CharField(max_length=30, null= True)
    f4sps_cp_addr = models.CharField(max_length=30, null= True)
    pst4sps = models.CharField(max_length=30, null= True)
    pst4sps_cp = models.CharField(max_length=30, null= True)
    pst4sps_cp_phone = models.CharField(max_length=30, null= True)
    pst4sps_cp_addr= models.CharField(max_length=30, null= True)
    ay = models.CharField(max_length=30, null= True)
    confirm = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "1: TBL Education"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        
        return self.name

class TBL_Education_ApplicantAttendedSchool(models.Model):
    necta_applicants = models.ManyToManyField(TBL_App_NECTADetails)
    center_number = models.CharField(max_length=10, null= True,  blank=True, unique=True)
    center_name = models.CharField(max_length=10, null= True,  blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '2: TBL Education Applicant Attended Schools'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.center_name)

class TBL_Education_FormFourInfos(models.Model):
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete= models.DO_NOTHING, null = True,related_name="ed_form4_info_tbl_app_applicant")

    index_no = models.CharField(max_length=16)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    # add some more field here

    class Meta:
        verbose_name = '3: TBL Eduction Form four infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.index_no


class TBL_Education_FormSixInfos(models.Model):
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete= models.DO_NOTHING, null = True,related_name="ed_form6_info_tbl_app_applicant")
    # add some more field here
    index_no = models.CharField(max_length=16)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '4:TBL Eduction Form Six infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.index_no

class TBL_Education_DiplomaInfos(models.Model):
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete= models.DO_NOTHING, null = True,related_name="ed_diploma_info_tbl_app_applicant")
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    # add some more field here

    class Meta:
        verbose_name = '5:TBL Eduction Diploma infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Diploma Infomations'

class TBL_Education_TertiaryEducationInfos(models.Model):
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete= models.DO_NOTHING, null = True,related_name="ed_te_info_tbl_app_applicant")
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = '6:TBL Tertiary Education infos'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        return "Tertiary Education"


class TBL_Education_institution(models.Model):

    INSTITUTE_TYPE = (
        ('DIPLOMA', 'DIPLOMA'),
        ('HIGH_LEVEL_EDUCATION', 'HIGH LEVEL EDUCTION'),
    )

    institute_type = models.CharField(choices=INSTITUTE_TYPE, null=True, max_length=20)
    institute_name = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = "7: TBL Eduction Institute"
        verbose_name_plural =verbose_name
    def __str__(self):
        return self.name





