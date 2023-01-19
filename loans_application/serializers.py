
from rest_framework import  serializers
from . models import *

class SearchNectaApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TBL_App_InitialApplicantCategory
        fields = ['*']
