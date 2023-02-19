from rest_framework import serializers
from .models import *
class TblDemographicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model =TblDemographicsDetails
        fields = "__all__"

class TblDemoRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblRegions
        fields ="__all__"
class TblDemoDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDistrict
        fields = "__all__"