
from rest_framework import  serializers

from loans_application.none_serializers import NoneNectaApplicantSerializer
from .models import *
from education_info.models import TBL_Education_ApplicantAttendedSchool

class NectaApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_App_NECTADetails
        fields = '__all__'

class ApplicantTypeSerialize(serializers.ModelSerializer): 
    necta = NectaApplicantSerializer()
    none_necta = NoneNectaApplicantSerializer()
    class Meta:
        model =TBL_App_ApplicantType
        fields = '__all__'


class ApplicantDetailsSerializer(serializers.ModelSerializer):
   applicant_type = ApplicantTypeSerialize()
   class Meta:
        model = TBL_App_ApplicantDetails
        fields = ["applicant_type",'email','phonenumber', 'created_at', 'updated_at']

class ApplicantCategoriesSerialixer(serializers.ModelSerializer):
     class Meta:
        model = TBL_App_Categories
        fields = "__all__"

class ApplicantSerializer(serializers.ModelSerializer):
        application_category = ApplicantCategoriesSerialixer()
        applicant_details = ApplicantDetailsSerializer()
        class Meta:
            model = TBL_App_Applicant
            fields = "__all__"
        # depth = 1

class PaymentSerializer(serializers.ModelSerializer):
        applicant = ApplicantSerializer()
        class Meta:
            model = TBL_App_PaymentDetails
            fields = "__all__"
      


