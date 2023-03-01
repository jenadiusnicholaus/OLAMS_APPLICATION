from datetime import timezone

from django.db import models
from loans_application.models import *
from applicantProfile.models import *


class TblPost4EductionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "1: TBL post 4 type"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_post_4_education_type'

    def __str__(self) -> str:
        return self.name


class TBL_EducationInfo(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(
        TblAppProfile, on_delete=models.CASCADE, null=True, related_name="ed_tbl_app_applicant")
    f4_no_of_seat = models.IntegerField(default=0)
    pst4ed = models.ForeignKey(TblPost4EductionType, on_delete=models.CASCADE,
                               null=True, related_name="ed_post_4_eduction_type_set")
    f4sps = models.BooleanField(default=False)

    pst4sps = models.BooleanField(default=False)

    app_year = models.CharField(max_length=30, null=True)
    confirm = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "2: TBL Education"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_education_info'

    def __str__(self):

        return str(self. id)


class TblSponsorDetails(models.Model):
    id = models.AutoField(primary_key=True)
    SPOSORED_CHOISES = (
        (0, "POST fORM fOUR SPONSORSHIP"),
        (1, "fORM fOUR SPONSORSHIP"),
    )

    sponsored_ed_type = models.CharField(
        choices=SPOSORED_CHOISES, max_length=20, null=True)
    applicant = models.ForeignKey(
        TblAppProfile, on_delete=models.CASCADE, null=True, related_name="ed_tbl_sps_set")
    sponsor_contact_person_full_name = models.CharField(
        max_length=30, null=True)
    sponsor_contact_person_phone_nunber = models.CharField(
        max_length=30, null=True)
    sponsor_contact_person_address = models.CharField(max_length=40, null=True)
    app_year = models.CharField(max_length=4, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "3: TBL Sponsor"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_sponsor_education_info'

    def __str__(self):

        return str(self.id)


class TBL_Education_ApplicantAttendedSchool(models.Model):
    id = models.AutoField(primary_key=True)
    necta_applicants = models.ManyToManyField(TBL_App_NECTADetails)
    center_number = models.CharField(
        max_length=10, null=True,  blank=True, unique=True)
    center_name = models.CharField(max_length=100, null=True,  blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '4: TBL Education Applicant Attended Schools'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_secondary_schools'

    def __str__(self):
        return str(self.center_name)


class TBL_Education_FormFourInfos(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.CASCADE,
                                  null=True, related_name="ed_form4_info_tbl_app_applicant")
    app_year = models.CharField(max_length=4, null=True)
    second_seat_index_no = models.CharField(max_length=16, null=True)
    third_seat_index_no = models.CharField(max_length=16, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    # add some more field here

    class Meta:
        verbose_name = '5: TBL Eduction Form four infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_form_four_details'

    def __str__(self):
        return self.index_no


class TBLEducationFormSixInfos(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.CASCADE,
                                  null=True, related_name="ed_form6_info_tbl_app_applicant")
    app_year = models.CharField(max_length=4, null=True)
    # add some more field here
    f6index_no = models.CharField(max_length=16)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '6:TBL Eduction Form Six infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_form_six_details'

    def __str__(self):
        return self.f6index_no


class TblDiplomaInstitutions(models.Model):
    id = models.AutoField(primary_key=True)
    INSTITUTE_TYPE = (
        ('DIPLOMA', 'DIPLOMA'),
        ('HIGH_LEVEL_EDUCATION', 'HIGH LEVEL EDUCTION'),
    )

    institute_type = models.CharField(
        choices=INSTITUTE_TYPE, null=True, max_length=20)
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


class TblDiplomaDetails(models.Model):
    id = models.AutoField(primary_key=True)
    app_year = models.CharField(max_length=4, null=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.CASCADE, null=True,
                                  related_name="ed_diploma_info_tbl_app_applicant")
    avn = models.CharField(max_length=60, null=True)
    entryYear = models.CharField(max_length=10, null=True)
    graduateYear = models.CharField(max_length=10, null=True)
    gpa = models.FloatField(null=True,
                            default=0.0)
    registrationNumber = models.CharField(max_length=60, null=True)
    diplomaInstitution = models.ForeignKey(TblDiplomaInstitutions, on_delete=models.DO_NOTHING, null=True,
                                           related_name="ed_diploma_institution")
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    # add some more field here

    class Meta:
        verbose_name = '9:TBL Eduction Diploma infos '
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_diploma_details'

    def __str__(self):
        return 'Diploma Infomations'


class Institutions(models.Model):
    id = models.IntegerField(primary_key=True)
    institutionName = models.CharField(
        max_length=100, db_column='institution_name')
    institutionCode = models.CharField(
        max_length=100, db_column='institution_code')
    geoLocated = models.BooleanField(
        db_column='geo_located', null=True, blank=True, default=False)
    active = models.CharField(max_length=100, db_column='active')

    def __str__(self):
        return self.institutionName

    class Meta:
        # verbose_name = 'DidisRegister',
        # verbose_name_plural = 'DidisRegisters'
        db_table = 'tbl_institutions'
        managed = False


class TBL_Education_TertiaryEducationInfos(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, on_delete=models.CASCADE,
                                  null=True, related_name="ed_te_info_tbl_app_applicant")
    admittedInstitute = models.ForeignKey(
        Institutions, on_delete=models.DO_NOTHING, null=False, )
    admittedCourse = models.ForeignKey(
        TblCourses, null=False, on_delete=models.DO_NOTHING)
    admittedDegreeCategory = models.CharField(
        null=False, default="Master", max_length=15)
    applicationYear = models.IntegerField(null=False, default="2023")
    confirm = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '10:TBL Tertiary Education infos'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_tertiary_education'

    def __str__(self):
        return self.admittedInstitute


class TblTertiaryEducationBachelorAwards(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, null=True, on_delete=models.DO_NOTHING,
                                  related_name="TblAwards_TertiaryInfo")
    award = models.CharField(max_length=50, null=False)
    regno = models.CharField(max_length=40)
    entryYear = models.IntegerField(null=False)
    graduateYear = models.IntegerField(null=False)
    gpa = models.FloatField(null=False)
    app_year = models.CharField(max_length=4, null=True)
    institution = models.ForeignKey(Institutions, null=False, related_name="TblAwardsInstitution",
                                    on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "9. Tertiary Education Bachelor Award"
        verbose_name_plural = verbose_name
        db_table = 'tbl_tertiary_education_bachelor_awards'

    def __str__(self):
        return self.award


class TblTertiaryEducationMasterAward(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TblAppProfile, null=True, on_delete=models.DO_NOTHING,
                                  related_name="TblMasterAwards_Applicant")
    master_award = models.CharField(max_length=50, null=False)
    regNo = models.CharField(max_length=40)
    entryYear = models.IntegerField(null=False)
    graduateYear = models.IntegerField(null=False)
    gpa = models.FloatField(null=False)
    app_year = models.CharField(max_length=4, null=True)
    institution = models.ForeignKey(Institutions, null=False, related_name="TblMasterAwardsInstitution",
                                    on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "11. Master Awards"
        verbose_name_plural = verbose_name
        db_table = 'tbl_tertiary_education_master_awards'
