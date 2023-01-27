
from .models import *
from rest_framework import serializers 
from loans_application.none_serializers import *

class SearchedNectaApplicationSerializer(serializers.ModelSerializer):
    necta_applicants = NoneNectaApplicantSerializer(many=True)
    class Meta:
        model = TBL_Education_ApplicantAttendedSchool
        fields = "__all__"

