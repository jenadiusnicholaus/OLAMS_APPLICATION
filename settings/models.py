from django.db import models
from django.utils import timezone


# Create your models here.
class OlamsConfigurations(models.Model):
    id = models.AutoField(primary_key=True)
    configurationName = models.CharField(max_length=100, null=False, unique=True)
    configurationValue = models.CharField(max_length=260, null=False)
    createdBy = models.CharField(max_length=100, null=False)
    created_date =models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name ="1: Olams Configurations"
        verbose_name_plural = verbose_name
        db_table ="tbl_olams_configurations"
    def __str__(self):
        return  self.configurationName + " "+ self.configurationValue
    
class UserApplicationStateManager(models.Model):

    APPLICATION_FORM_FILLING_STATUS = (

        ( 1, "APPLLICATION_FEE_AND_PAYMENTS",), 
        ( 2, "SELF_REGISTRATION",),
        ( 3, "APPLICATION_CATEGORY",),
        ( 4, "APPLICANT_BASIC_INFO",),
        ( 5, "DEMOGRAPHICS_INFO",),  
        ( 6, "PRELIMINARY_INFO",),
        ( 7, "EDUCATION_INFO",), 
        ( 8, "GUARANTOR_INFO",), 

        )
    MENU_STATE = (

        ( 'DONE', "DONE",), 
        ( 'IN_PROGRESS', "IN PROGRESS",),
        ( 'nOT_STARTED', "NOT STARTED",),
      
    )
    
    
    menu_id =  models.IntegerField(null = True )
    proocess_name = models.IntegerField(choices=APPLICATION_FORM_FILLING_STATUS)
    menu_state =  models.CharField(choices=MENU_STATE, max_length= 200)

    class Metan:
        verbose_name = '2: Application state'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.proocess_name


    

    