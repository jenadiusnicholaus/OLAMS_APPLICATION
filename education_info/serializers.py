
from .models import *
from rest_framework import serializers 
from loans_application.none_necta_serializers import *
from loans_application.necta_serializers import *

class ApplicantSchoolInformationSerializer(serializers.ModelSerializer):
    necta_applicants = NectaApplicantSerializer(many=True)
    class Meta:
        model = TBL_Education_ApplicantAttendedSchool
        fields = "__all__"

