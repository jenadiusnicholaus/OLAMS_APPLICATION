
import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from utils.constants import Constants


class  TBL_App_NECTADetails(models.Model):
    id = models.AutoField(primary_key=True)
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
        verbose_name = '1.0: TBL App Applicants NECTA User Details'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_necta_details'

    def __str__(self):
        return self.first_name

class  TBL_App_NoneNECTADetails(models.Model):
    id = models.AutoField(primary_key=True)
    SEX = (('MALE', 'Male'),('FEMALE', 'Female'))
    index_no =  models.CharField(max_length= 16, unique=True, null=True, blank=True, editable=False)
    original_no = models.CharField(max_length= 30, null=True, unique=True)
    first_name = models.CharField(max_length= 16, null=True)
    middle_name = models.CharField(max_length= 16, null=True)
    last_name = models.CharField(max_length= 16, null= True)
    app_year = models.CharField(max_length= 16, null=True)
    exam_year = models.CharField(max_length= 16, null=True)
    sur_name = models.CharField(max_length= 16,null=True)
    sex = models.CharField(max_length=20, choices=SEX, null=True, blank=False )
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    created_at = models.DateTimeField(default=timezone.now,null=True)
    changed_necta = models.BooleanField(default=False, null=True)
   

    class Meta:
        verbose_name = '1.1: TBL App Applicants None NECTA User Details'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_non_necta_details'

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
    id = models.AutoField(primary_key=True)
    """
     Initially the applicant category can be necta on none necta
    """
    necta =  models.ForeignKey(TBL_App_NECTADetails, on_delete=models.DO_NOTHING, related_name='tbl_app_necta_applicant', null = True, blank=True)
    none_necta =  models.ForeignKey(TBL_App_NoneNECTADetails, on_delete=models.DO_NOTHING, related_name='tbl_none_app_necta_applicant', null = True, blank=True)
    description= models.TextField(null= True,  blank= True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '2: TBL App ApplicantType'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_type'


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
    id = models.AutoField(primary_key=True)
    applicant_type = models.ForeignKey(TBL_App_ApplicantType, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='tbl_app_initial_applicant_type')
    phonenumber = models.CharField(max_length= 15, null= False, blank=False)
    email = models.EmailField(max_length= 30,null = True, blank=True)
    appYear = models.CharField(max_length=4, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
 
    class Meta:
        verbose_name = '3: TBL App Applicant Details'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_applicants_details'
        
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
    if created:
        try:
            TBL_App_ApplicantDetails.objects.update_or_create(
                applicant_type = instance)
        except Exception as ex:
            raise
    
        
class TBL_App_Categories(models.Model):
    id: int = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null = True,blank=True)
    description = models.TextField( null = True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = "4: TBL App  Applicants Categories"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_applicant_category'

    def __str__(self):
        return self.name


class TBL_App_Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    applicant_details = models.ForeignKey(TBL_App_ApplicantDetails,  on_delete=models.DO_NOTHING, related_name='tbl_app_applicant_details')
    application_category = models.ForeignKey(TBL_App_Categories, on_delete=models.DO_NOTHING, related_name='tbl_app_applicant_category' )
    app_year = models.CharField(max_length=4, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
   
    class Meta:
        verbose_name = '5: TBL Applicant Conso Tbl'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_applicants'

    def __str__(self):
        if self.applicant_details is not None and self.applicant_details.applicant_type.none_necta is None:
            return self.applicant_details.applicant_type.necta.first_name
        return self.applicant_details.applicant_type.none_necta.original_no


class TBL_App_PaymentDetails(models.Model):
    id = models.AutoField(primary_key=True)
    PAYMENY_STATUS = ((0, 'Not Paid'), (1, 'Paid'))
    USED_STATUS =  ((0, 'Not used'), (1, 'Used'))
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete=models.DO_NOTHING, related_name='tbl_app_applicant', null=True)
    payment_status =  models.IntegerField(choices=PAYMENY_STATUS, default=0,  null=True)
    control_number = models.CharField(max_length=30, null=True, blank=True )
    reference =  models.CharField(max_length=30, null=True, blank=True )
    paid_when =  models.DateTimeField( null=True, blank=True )
    amount_paid = models.CharField(max_length=20, null=True, blank=True )
    used_by = models.CharField(max_length=16, null=True, blank=True)
    used_when = models.DateTimeField(max_length=16, null=True, blank=True )
    used_status = models.IntegerField(choices = USED_STATUS, default=0, null= True, blank=True )
    app_year = models.CharField(max_length=4, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = "6: TBL App Payment Details"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name
        db_table = 'tbl_application_payment_details'

    def __str__(self):
        if self.applicant:
            if self.used_by is not None:
                return self.used_by
            elif self.applicant.applicant_details.applicant_type.necta:
                return self.applicant.applicant_details.applicant_type.necta.first_name
            else:
                return self.applicant.applicant_details.applicant_type.none_necta.first_name
        else:
            return 'None'
    def save(self, *args, **kwargs):
        if self.applicant.applicant_details.applicant_type.necta :
            self.used_by = self.applicant.applicant_details.applicant_type.necta.index_no
            return super(TBL_App_PaymentDetails, self,).save(*args, **kwargs) 
        elif self.applicant.applicant_details.applicant_type.none_necta:
            self.used_by = self.applicant.applicant_details.applicant_type.none_necta.index_no
            return super(TBL_App_PaymentDetails, self,).save(*args, **kwargs) 
            
        
@receiver(post_save, sender=TBL_App_Applicant)
def create_or_update_applicant_details(sender, instance, created, **kwargs):
    if created:
        try:
            TBL_App_PaymentDetails.objects.update_or_create(
                applicant = instance)
        except Exception as ex:
            raise
    



    
    
    








     









