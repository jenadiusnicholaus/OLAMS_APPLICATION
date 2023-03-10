import os
from django.db import models
from loans_application.models import *
from django.utils import timezone

class TblAppProfile(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete=models.DO_NOTHING,
                                  related_name='tbl_app_applicant_profile_set', null=True)
    user = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, related_name='user_profile_set', null=True)
    secret_question = models.CharField(max_length=100, null=True, blank=True)
    secret_answer = models.CharField(max_length=100, null=True, blank=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "7: Applicant Profile"
        verbose_name_plural = verbose_name
        db_table = 'tbl_applicant_profile'

    def __str__(self):

        if self.user:
            return self.user.username
        elif self.applicant.applicant_details.applicant_type.necta:
            return self.applicant.applicant_details.applicant_type.necta.first_name
        elif self.applicant.applicant_details.applicant_type.none_necta:
            return self.applicant.applicant_details.applicant_type.none_necta.first_name


@receiver(post_save, sender=TBL_App_Applicant)
def create_or_update_applicant_inst_profile(sender, instance, created, **kwargs):
    if created:
        try:
            TblAppProfile.objects.update_or_create(
                applicant=instance)
        except Exception as ex:
            raise ex


class ApplicantPhoto(models.Model):
    id = models.AutoField(primary_key=True)
    applicant_id = models.OneToOneField(TblAppProfile, on_delete=models.DO_NOTHING,
                                        related_name='tbl_app_applicant_photo_set', null=True)

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("applicant",  self.applicant_id.user.username, instance)
        return None
    photo = models.ImageField(upload_to=image_upload_to, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name = "7: Applicant Photo"
        verbose_name_plural = verbose_name
        db_table = 'tbl_applicant_photo'

    def __str__(self):
        if self.applicant_id:
            return self.applicant_id.user.username
        return str('Error insertion')
