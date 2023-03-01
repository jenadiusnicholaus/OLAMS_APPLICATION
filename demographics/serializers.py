from rest_framework import serializers
from .models import *
from loans_application.necta_serializers import UserProfileSerialiozer


class TblDemoRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblRegions
        fields = "__all__"
        read_only_fields = ('id',)


class TblDemoDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDistrict
        fields = "__all__"
        read_only_fields = ('id',)


class ConfirmDemographicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDemographicsDetails
        fields = 'confirm',


class TblDemographicDetailsSerializer(serializers.ModelSerializer):
    region = TblDemoRegionSerializer(read_only=True)
    distric = TblDemoDistrictSerializer(read_only=True)
    region = TblDemoRegionSerializer(read_only=True)
    dom_region = TblDemoRegionSerializer(read_only=True)
    dom_distric = TblDemoDistrictSerializer(read_only=True)
    applicant = UserProfileSerialiozer(read_only=True)

    class Meta:
        model = TblDemographicsDetails
        fields = "__all__"

    def update(self, instance, validated_data):
        region_data = validated_data.pop('region', None)
        district_data = validated_data.pop('distric', None)
        dom_region_data = validated_data.pop('dom_region', None)
        dom_district_data = validated_data.pop('dom_distric', None)

        if region_data:
            region_serializer = TblDemoRegionSerializer(
                instance.region, data=region_data)
            if region_serializer.is_valid():
                region_serializer.save()

        if district_data:
            district_serializer = TblDemoRegionSerializer(
                instance.district, data=district_data, partial=True)
            if district_serializer.is_valid():
                district_serializer.save()

        if dom_region_data:
            dom_region_serializer = TblDemoRegionSerializer(
                instance.dom_region, data=dom_region_data,  partial=True)
            if dom_region_serializer.is_valid():
                dom_region_serializer.save()

        if dom_district_data:
            dom_district_serializer = TblDemoRegionSerializer(
                instance.dom_district, data=dom_district_data,  partial=True)
            if dom_district_serializer.is_valid():
                dom_district_serializer.save()

        return super().update(instance, validated_data)
