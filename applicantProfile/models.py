from django.db import models
from loans_application.models import *
from django.utils import timezone
# Create your models here.

class TblAppProfile(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(TBL_App_Applicant, on_delete=models.DO_NOTHING, related_name='tbl_app_applicant_profile_set', null=True)
    user = models.OneToOneField(User,on_delete= models.DO_NOTHING, related_name= 'user_profile_set', null=True)
    secret_question = models.CharField(max_length = 100, null = True, blank=True )
    secret_answer = models.CharField(max_length = 100, null = True, blank=True )
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


# updated user profile when applicant is created
@receiver(post_save, sender=TBL_App_Applicant)
def create_or_update_applicant_inst_profile(sender, instance, created, **kwargs):
    if created:
        try:
            TblAppProfile.objects.update_or_create(
                applicant=instance)
        except Exception as ex:
            raise ex
