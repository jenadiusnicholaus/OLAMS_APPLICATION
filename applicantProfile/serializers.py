from rest_framework import serializers
from .models import *
class TblApplicantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =TBL_App_Profile
        fields ="__all__"