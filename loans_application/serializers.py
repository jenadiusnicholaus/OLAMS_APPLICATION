
from rest_framework import  serializers
from . models import *

class NectaApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_App_NECTADetails
        fields = '__all__'

class NoneNectaApplicantSerialize(serializers.ModelSerializer):
    class Meta:
        model = TBL_App_NoneNECTADetails
        fields = '__all__'

class ApplicantTypeSerialize(serializers.ModelSerializer): 
    necta = NectaApplicationSerializer()
    none_necta = NoneNectaApplicantSerialize()
    class Meta:
        model =TBL_App_ApplicantType
        fields = '__all__'



class SearchedNectaApplicationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TBL_App_ApplicantAttendedSchool
        fields = ['center_number','center_name','center_number','updated_at','updated_at']


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
        # applicant_details = serializers.HyperlinkedRelatedField(many=True, view_name='applicant_details', read_only=True)
        application_category = ApplicantCategoriesSerialixer()
        applicant_details = ApplicantDetailsSerializer()
        class Meta:
            model = TBL_App_Applicant
            fields = "__all__"
        # depth = 1

