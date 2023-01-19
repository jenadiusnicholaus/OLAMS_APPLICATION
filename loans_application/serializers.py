
from rest_framework import  serializers
from . models import *

class NectaApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_App_NECTADetails
        fields = '__all__'
class SearchedNectaApplicationSerializer(serializers.ModelSerializer):
    necta_applicants = NectaApplicationSerializer(many=True)
 
    class Meta:
        model = TBL_App_ApplicantAttendedSchool
        fields = ['center_number','center_name','center_number','updated_at','updated_at']
