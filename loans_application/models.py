
import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from utils.constants import Constants


class  TBL_App_NECTADetails(models.Model):
    SEX = (('MALE', 'Male'),('FEMALE', 'Female'))
    NECTA_STUDENT_ED_LEVEL_STATUS = (('FORM_4', 'FORM FOUR'),('FORM_6', 'FORM SIX'),)
    index_no = models.CharField(max_length = 16, unique = False, null=True, blank=True)
    education_level = models.CharField(max_length = 16,choices = NECTA_STUDENT_ED_LEVEL_STATUS, null = True)
    first_name = models.CharField(max_length = 16, null= False, blank=True)
    middle_name = models.CharField(max_length = 16, null= False, blank=True)
    sur_name = models.CharField(max_length = 16, null= False, blank=True)
    app_year = models.CharField(max_length= 16, null= True)
    last_name = models.CharField(max_length= 16, null= True)
    exam_year = models.CharField(max_length= 16, null=True)
    sex = models.CharField(max_length=20, choices=SEX, null=True, blank=False )
    updated_at = models.DateTimeField(default = timezone.now)
    created_at = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App Applicants NECTA User Details'

    def __str__(self):
        return self.first_name

class  TBL_App_NoneNECTADetails(models.Model):
    SEX = (('MALE', 'Male'),('FEMALE', 'Female'))
    index_no =  models.CharField(max_length= 16, unique=True, null=True, blank=True, editable=False)
    original_no = models.CharField(max_length= 30)
    first_name = models.CharField(max_length= 16)
    middle_name = models.CharField(max_length= 16)
    last_name = models.CharField(max_length= 16, null= True)
    app_year = models.CharField(max_length= 16, null=True)
    exam_year = models.CharField(max_length= 16, null=True)
    sur_name = models.CharField(max_length= 16)
    sex = models.CharField(max_length=20, choices=SEX, null=True, blank=False )
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    changed_necta = models.BooleanField(default=False)
   

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App Applicants None NECTA User Details'

    def __str__(self):
        return str(self.index_no)

    @property
    def _id(self):
        return self.id

    def index_no_id(self, id):
        number = f"{random.randint(1,1000)}".zfill(4)
        return str(number)
      

    def two_last_digts_of_app_year(self):
        if self.app_year is None:
            return str(Constants.current_year)[-2:]
        return str(self.app_year)[-2:]

    def get_exam_year(self):
        if self.exam_year  is not None:
            return str(self.exam_year)
        self.exam_year = str(self.original_no)[-4:]
        return str(self.original_no)[-4:]
        
    def generate_index_number(self):
        _new_index_no =  f'E00{self.two_last_digts_of_app_year()}.{self.index_no_id(self.id)}.{self.get_exam_year()}'
        return _new_index_no

    def assign_the_index_no(self):
        self.index_no = self.generate_index_number()

    def save(self, *args, **kwargs):
        if self.original_no is not None and self.index_no is None:
            self.assign_the_index_no()
            return super(TBL_App_NoneNECTADetails, self,).save(*args, **kwargs)


class TBL_App_ApplicantType(models.Model):
    """
     Initially the applicant category can be necta on none necta
    """
    necta =  models.ForeignKey(TBL_App_NECTADetails, on_delete=models.DO_NOTHING, related_name='tbl_app_necta_applicant', null = True, blank=True)
    none_necta =  models.ForeignKey(TBL_App_NoneNECTADetails, on_delete=models.DO_NOTHING, related_name='tbl_none_app_necta_applicant', null = True, blank=True)
    description= models.TextField(null= True,  blank= True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App ApplicantType'


    def __str__(self):
        if self.none_necta == None:
            return self.necta.first_name
        return str(self.none_necta.original_no)


@receiver(post_save, sender=TBL_App_NoneNECTADetails)
def create_or_update_applicant_type(sender, instance, created, **kwargs):
    if created:
        try:
            TBL_App_ApplicantType.objects.update_or_create(
                none_necta = instance)
        except Exception as ex:
            raise


        
class TBL_App_ApplicantDetails(models.Model):
    applicant_type = models.ForeignKey(TBL_App_ApplicantType, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='tbl_app_initial_applicant_type')
    phonenumber = models.CharField(max_length= 15, null= False, blank=False)
    email = models.EmailField(max_length= 30,null = True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
 
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App Applicant Details'
        
    def __str__(self):
        if  self.applicant_type:  
            if self.applicant_type.necta !=  None:
           
                return self.applicant_type.necta.first_name
            else:
                if self.applicant_type.none_necta.first_name:
                    return self.applicant_type.none_necta.first_name
                return self.applicant_type.none_necta.original_no
               

@receiver(post_save, sender=TBL_App_ApplicantType)
def create_or_update_applicant_details(sender, instance, created, **kwargs):
    # for each subject, add class in the table of subjectClass
    if created:
        try:
            TBL_App_ApplicantDetails.objects.update_or_create(
                applicant_type = instance)
        except Exception as ex:
            raise
    
        
class TBL_App_Categories(models.Model):
    name = models.CharField(max_length=20, null = True,blank=True)
    description = models.TextField( null = True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App  Applicants Categories'

    def __str__(self):
        return self.name


class TBL_App_Applicant(models.Model):
    applicant_details = models.ForeignKey(TBL_App_ApplicantDetails,  on_delete=models.DO_NOTHING, related_name='tbl_app_applicant_details')
    application_category = models.ForeignKey(TBL_App_Categories, on_delete=models.DO_NOTHING, related_name='tbl_app_applicant_category' )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App Applicants'

    def __str__(self):
        if self.applicant_details is not None and self.applicant_details.applicant_type.none_necta is None:
            return self.applicant_details.applicant_type.necta.first_name
        return self.applicant_details.applicant_type.none_necta.firt_name


class TBL_App_PaymentDetails(models.Model):
    PAYMENY_STATUS = (('no_paid', 'Not Paid'), ('paid', 'Paid'))
    USED_STATUS =  (('not_used', 'No used'), ('used', 'used'))
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete=models.DO_NOTHING, related_name='tbl_app_applicant', null=True)
    payment_status =  models.CharField(max_length=20 ,choices=PAYMENY_STATUS, default=0)
    control_number = models.CharField(max_length=30, null=False, blank=False )
    reference =  models.CharField(max_length=30, null=False, blank=False )
    paid_when =  models.DateTimeField( null=False, blank=False )
    used_by = models.CharField(max_length=16, null=True, blank=False)
    used_when = models.DateTimeField(max_length=16, null=False, blank=False )
    used_status = models.CharField(max_length=16, choices=USED_STATUS, null= False, blank=False )
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App Payment Details'

    def __str__(self):
        if self.used_by is None:
            return None
        return 'TBL App Aayment Details'

class TBL_App_ApplicantAttendedSchool(models.Model):
    necta_applicants = models.ManyToManyField(TBL_App_NECTADetails)
    center_number = models.CharField(max_length=10, null= True,  blank=True, unique=True)
    center_name = models.CharField(max_length=10, null= True,  blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App Applicant Attended Schools'

    def __str__(self):
        return self.center_number
     









