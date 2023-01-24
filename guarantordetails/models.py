import os
from django.db import models
from loans_application.models import *
from demographics.models import *
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class TBL_GuarantorDetailsLUG(models.Model):
    SEX = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),

    )

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("GuarantorDetailsLUG", self.user.username, instance)
        return None

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_guarantor_details")
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete= models.DO_NOTHING, null = True,related_name="guarantor_tbl_app_applicant")
    sur_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null = True)
    sex = models.CharField(max_length=10, null =True, choices=SEX)
    region = models.ForeignKey(TBL_Demo_Region, on_delete=models.DO_NOTHING, null= True, related_name="guarantor_region_lug")
    district = models.ForeignKey(TBL_Demo_Region, on_delete=models.DO_NOTHING, null= True, related_name="guarantor_district")
    postaladdress = models.CharField(max_length=10, null =True)
    mobile = PhoneNumberField(blank=True, null = True)
    email = models.CharField(max_length=10, null =True)
    ward = models.CharField(max_length=10, null =True)
    village = models.CharField(max_length=10, null =True)
    idcardnumber = models.CharField(max_length=10, null =True)
    cardtype = models.CharField(max_length=10, null =True)
    photo = models.FileField(max_length=10, null =True, upload_to=image_upload_to)
   
    ay = models.CharField(max_length=10, null =True),
    photoverified = models.BooleanField(default=False)
    referenceId = models.CharField(max_length=10, null =True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now) 
    confirm = models.CharField(max_length=10, null =True)

    class Meta:
        verbose_name = '1: Guarant details LUG'
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.user.username:
            return self.user.username
        return self.user.first_name

class TBL_GuarantorDetailsPGD(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_guarantor_details_pgd")
    postaladdress = models.CharField(max_length=100)
    telephone = PhoneNumberField(null=True)

    contact_title = models.CharField(max_length=20, null=True)

    # need some explaination
    inst = models.CharField(max_length=20, null=True)
    region = models.ForeignKey(TBL_Demo_Region, on_delete=models.DO_NOTHING, null= True, related_name="guarantor_region_pgd")
    
    district = models.ForeignKey(TBL_Demo_District, on_delete=models.DO_NOTHING, null= True, related_name="guarantor_district_pgd")
     
    contactperson = models.CharField(max_length=20, null= True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now) 
    
    #  need some explainations
    ay = models.CharField(max_length=20, null= True)
    confirm = models.CharField(max_length=10, null =True)

    

    class Meta:
        verbose_name = "2: Tbl Guarantor details PGD"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.first_name

   

    