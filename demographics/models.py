from django.db import models
from django.utils import timezone

from loans_application.models import *


class TBL_Demo_DemocileDetails(models.Model):
    applicant = models.ForeignKey(TBL_App_Profile, on_delete= models.DO_NOTHING, null = True,related_name="demo_tbl_app_applicant")
    dob = models.DateField( null=True)
    region = models.ForeignKey('TBL_Demo_Region', on_delete= models.DO_NOTHING, null = True, related_name="demo_tbl_demo_region")
    distric = models.ForeignKey('TBL_Demo_District', on_delete=models.DO_NOTHING, null=True)
    disability = models.BooleanField(default=False)
    dom_region = models.ForeignKey("TBL_Demo_Region", on_delete=models.DO_NOTHING, related_name='demo_domestic_region', null=True)
    dom_distric = models.ForeignKey("TBL_Demo_District", on_delete=models.DO_NOTHING, related_name='demo_domestic_distric', null=True)
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
        db_table = 'tbl_application_demographics_details'


    def __str__(self):
        
        return self.name

class TBL_Demo_Region(models.Model):
    region_id = models.IntegerField(null=False, blank=False, primary_key=True,default=111)
    region_name = models.CharField(null=True, blank=False, unique=True, max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "2: TBL Demo Region"
        ordering = ['-created_date']
        verbose_name_plural = verbose_name
        db_table = 'tbl_regions'

    def __str__(self):
        
        return f'{self.region_name}'

class TBL_Demo_District(models.Model):
    region = models.ForeignKey(TBL_Demo_Region, null=True, blank=False, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "3: TBL Demo District"
        ordering = ['-created_date']
        verbose_name_plural = verbose_name
        db_table = 'tbl_districts'

    def __str__(self):
        return self.region.region_name + '-' + self.district_name