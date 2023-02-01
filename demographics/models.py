from django.db import models
from django.utils import timezone

from loans_application.models import *


class TBL_Demo_DemocileDetails(models.Model):
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete= models.DO_NOTHING, null = True,related_name="demo_tbl_app_applicant")
    dob = models.DateField( null=True)
    region = models.ForeignKey('TBL_Demo_Region', on_delete= models.DO_NOTHING, null = True, related_name="demo_tbl_demo_region")
    distric = models.ForeignKey('TBL_Demo_District', on_delete=models.DO_NOTHING, null=True)
    disability = models.BooleanField(default=False)
    dom_region = models.ForeignKey("TBL_Demo_Region", on_delete=models.DO_NOTHING, related_name='demo_domestic_region')
    dom_distric = models.ForeignKey("TBL_Demo_District", on_delete=models.DO_NOTHING, related_name='demo_domestic_distric')
    dom_postal  = models.CharField(max_length=50, null = True)
    dom_ward = models.CharField(max_length=50, null = True)
    birth_cert_no = models.CharField(max_length=50, null = True)
    cert_type_id = models.CharField(max_length=50, null = True)
    nationalIdNo = models.CharField(max_length=50, null = True)
    birthplace = models.CharField(max_length=50, null = True)
    dom_village = models.CharField(max_length=30 , null= True)

    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name = "1: TBL Demo Democile Details"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name


    def __str__(self):
        
        return self.name

class TBL_Demo_Region(models.Model):
    name = models.CharField(max_length=50, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "2: TBL Demo Region"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        
        return self.name

class TBL_Demo_District(models.Model):
    name = models.CharField(max_length=50, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "3: TBL Demo District"
        ordering = ['-created_at']
        verbose_name_plural = verbose_name

    def __str__(self):
        
        return self.name