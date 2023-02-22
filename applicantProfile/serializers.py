from rest_framework import serializers
from .models import *
class TblApplicantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =TblAppProfile
        fields ="__all__"