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
        verbose_name ="Olams Configurations"
        verbose_name_plural = verbose_name
        db_table ="tbl_olams_configurations"
    def __str__(self):
        return  self.configurationName + " "+ self.configurationValue