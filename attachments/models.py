import os

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone





class TBL_attachments(models.Model):
    STATUS = (
    ('',""),
    ('',""),
    )
    cycle = models.CharField(max_length = 30, null = True)
    docid = models.ForeignKey("TBL_AttachemetsDocs", on_delete=models.DO_NOTHING, related_name="attachement_doc")
    status = models.CharField(max_length=50, null = True)
    verification = models.BooleanField(default=False)
    filename = models.CharField(max_length=100, null=True)
    
    verifiedby = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    verifieddate = models.DateTimeField(auto_created=False)

    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    confirm = models.BooleanField(default=False)


    class Meta:
        verbose_name ="1: TBL Attachments Docs"
        verbose_name_plural =verbose_name
    def __str__(self):
        return self.name



    class Meta:
        verbose_name ="2: TBL Attachments Docs"
        verbose_name_plural =verbose_name
    def __str__(self):
        return self.name


class TBL_AttachemetsDocs(models.Model):

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("attachments", instance)
        return None
    file = models.FileField(upload_to=image_upload_to)
    
    class Meta:
        verbose_name ="2: TBL Attachments Docs"
        verbose_name_plural =verbose_name
    def __str__(self):
        return self.name

