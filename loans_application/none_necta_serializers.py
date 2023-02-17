
from rest_framework import  serializers
from .models import *


class NoneNectaApplicantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TBL_App_NoneNECTADetails
        fields = '__all__'
