
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import random

class  TBL_App_NECTADetails(models.Model):
    SEX = (('MALE', 'Male'),('FEMALE', 'Female'))
    NECTA_STUDENT_ED_LEVEL_STATUS = (('FORM_4', 'FORM FOUR'),('FORM_6', 'FORM SIX'),)
    index_no = models.CharField(max_length = 16, unique = True)
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
    index_no =  models.CharField(max_length= 16, unique=True)
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
        return self.index_no

    def __random_number(self):
        number = random.randint(1000,9999)
        return number
        
    def save(self, *args, **kwargs):
        if self.original_no is not None and self.index_no is None:
            two_digits_of_app_year = self.app_year % 100 
            # Todo: update on on the  dave by create ting applicnt index no
            new_index_no =  f'E00{two_digits_of_app_year}.{self.__random_number}.'
            self.index_no = new_index_no
            return super(TBL_App_NoneNECTADetails, self,).save(*args, **kwargs)

class TBL_App_InitialApplicantCategory(models.Model):
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
        verbose_name_plural = 'TBL App InitialApplicantCategory'


    def __str__(self):
        if self.none_necta == None:
            return self.necta.first_name
        return self.none_necta.first_name
        
class TBL_App_ApplicantDetails(models.Model):
    applicant_categories = models.ForeignKey(TBL_App_InitialApplicantCategory, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='tbl_app_initial_applicant_category')
    f4_indexno = models.CharField(max_length= 30, null=True, blank= False)
    sur_name = models.CharField(max_length=20, null=False, blank=False )
    middle_name = models.CharField(max_length=20, null=False, blank=False )
    phonenumber = models.CharField(max_length= 15, null= False, blank=False)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
 
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App Applicant Details'
        
    def __str__(self):
        if  self.applicant_categories is not None and   self.applicant_categories.necta !=  None:
           
            return self.applicant_categories.necta.first_name
        return self.applicant_categories.none_necta.first_name
    def save(self, *args, **kwargs):
        # if( self.applicant_categories is not None):

        return super().save(*args, **kwargs)
 
        
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


class TBL_App_Applicantion(models.Model):
    applicant_details = models.ForeignKey(TBL_App_ApplicantDetails,  on_delete=models.DO_NOTHING, related_name='tbl_app_applicant_details')
    application_category = models.ForeignKey(TBL_App_Categories, on_delete=models.DO_NOTHING, related_name='tbl_app_applicant_category' )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'TBL App Applicants'

    def __str__(self):
        if self.applicant_details is not None and self.applicant_details.applicant_categories.none_necta is None:
            return self.applicant_details.applicant_categories.necta.first_name
        return self.applicant_details.applicant_categories.none_necta.firt_name


class TBL_App_PaymentDetails(models.Model):
    PAYMENY_STATUS = (('no_paid', 'Not Paid'), ('paid', 'Paid'))
    USED_STATUS =  (('not_used', 'No used'), ('useed', 'used'))
    applicant = models.ForeignKey(TBL_App_Applicantion, on_delete=models.DO_NOTHING, related_name='tbl_app_applicant', null=True)
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
        
     
     
     


    






