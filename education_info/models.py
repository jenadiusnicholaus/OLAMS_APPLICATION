from datetime import timezone

from django.db import models
from loans_application.models import *

class TBL_EducationInfo(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TBL_App_Profile, on_delete= models.DO_NOTHING, null = True,related_name="ed_tbl_app_applicant")
    f4_no_of_seat = models.IntegerField(default=0)
    pst4ed = models.CharField(max_length=30, null=True)
    f4sps = models.CharField(max_length=30, null=True)
    f4sps_cp = models.CharField(max_length=30, null=True)
    f4sps_cp_phone = models.CharField(max_length=30, null=True)
    f4sps_cp_addr = models.CharField(max_length=30, null=True)
    pst4sps = models.CharField(max_length=30, null=True)
    pst4sps_cp = models.CharField(max_length=30, null=True)
    pst4sps_cp_phone = models.CharField(max_length=30, null=True)
    pst4sps_cp_addr = models.CharField(max_length=30, null=True)
    ay = models.CharField(max_length=30, null=True)
    confirm = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "1: TBL Education"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_education_info'

    def __str__(self):
        
        return self.name

class TBL_Education_ApplicantAttendedSchool(models.Model):
    id = models.AutoField(primary_key=True)
    necta_applicants = models.ManyToManyField(TBL_App_NECTADetails)
    center_number = models.CharField(max_length=10, null=True,  blank=True, unique=True)
    center_name = models.CharField(max_length=100, null=True,  blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '2: TBL Education Applicant Attended Schools'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_secondary_schools'

    def __str__(self):
        return str(self.center_name)

class TBL_Education_FormFourInfos(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TBL_App_Profile, on_delete=models.DO_NOTHING, null=True, related_name="ed_form4_info_tbl_app_applicant")

    index_no = models.CharField(max_length=16)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    # add some more field here

    class Meta:
        verbose_name = '3: TBL Eduction Form four infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_form_four_details'

    def __str__(self):
        return self.index_no


class TBL_Education_FormSixInfos(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TBL_App_Profile, on_delete=models.DO_NOTHING, null=True, related_name="ed_form6_info_tbl_app_applicant")
    # add some more field here
    index_no = models.CharField(max_length=16)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '4:TBL Eduction Form Six infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_form_six_details'

    def __str__(self):
        return self.index_no

class TBL_Education_DiplomaInfos(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TBL_App_Profile, on_delete=models.DO_NOTHING, null=True, related_name="ed_diploma_info_tbl_app_applicant")
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    # add some more field here

    class Meta:
        verbose_name = '5:TBL Eduction Diploma infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_diploma_details'

    def __str__(self):
        return 'Diploma Infomations'


class TBL_Education_institution(models.Model):
    id = models.AutoField(primary_key=True)
    INSTITUTE_TYPE = (
        ('DIPLOMA', 'DIPLOMA'),
        ('HIGH_LEVEL_EDUCATION', 'HIGH LEVEL EDUCTION'),
    )

    institute_type = models.CharField(choices=INSTITUTE_TYPE, null=True, max_length=20)
    institute_name = models.CharField(max_length=60, null=True)
    instituteCode = models.CharField(max_length=35, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "7: TBL Eduction Institute"
        verbose_name_plural = verbose_name
        db_table = 'tbl_diploma_institutions'

    def __str__(self):
        return self.institute_name


class TblCourses(models.Model):
    id = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=50, null=False)
    courseCode = models.CharField(max_length=30, null=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "8. TBL_COURSES"
        verbose_name_plural = verbose_name
        db_table = 'tbl_courses'

    def __str__(self):
        return self.courseCode


class TBL_Education_TertiaryEducationInfos(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TBL_App_Profile, on_delete=models.DO_NOTHING, null=True, related_name="ed_te_info_tbl_app_applicant")
    admittedInstitute = models.ForeignKey(TBL_Education_institution, on_delete=models.DO_NOTHING, null=False, )
    admittedCourse = models.ForeignKey(TblCourses, null=False, on_delete=models.DO_NOTHING)
    admittedDegreeCategory = models.CharField(null=False, default="Master", max_length=15)
    applicationYear = models.IntegerField(null=False, default="2023")
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '6:TBL Tertiary Education infos'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_tertiary_education'

    def __str__(self):
        return self.admittedInstitute


class TblTertiaryEducationAwards(models.Model):
    id = models.AutoField(primary_key=True)
    tertiaryInfo = models.ForeignKey(TBL_Education_TertiaryEducationInfos, null=True, on_delete=models.DO_NOTHING,
                                     related_name="TblAwards_TertiaryInfo")
    award = models.CharField(max_length=50, null=False)
    regno = models.CharField(max_length=40)
    entryYear = models.IntegerField(null=False)
    graduateYear = models.IntegerField(null=False)
    awardCategory = models.CharField(max_length=20, null=False)
    gpa = models.FloatField(null=False)
    institution = models.ForeignKey(TBL_Education_institution, null=False, related_name="TblAwardsInstitution",
                                    on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "9. Tertiary Education Award"
        verbose_name_plural = verbose_name
        db_table = 'tbl_tertiary_education_awards'

    def __str__(self):
        return self.award

class TblInstitutionCourse(models.Model):
    id = models.AutoField(primary_key=True)
    institution = models.ForeignKey(TBL_Education_institution, on_delete=models.DO_NOTHING, null=False)
    course = models.ForeignKey(TblCourses, on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name ="10: Institution Course"
        verbose_name_plural = verbose_name
        db_table = 'tbl_institutioncourses'

    def __str__(self):
        return self.institution + " " + self.course


