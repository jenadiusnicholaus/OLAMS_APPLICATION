from rest_framework import serializers
from .models import *


class TblApplicantProUploadImageSerializerfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAppProfile
        fields = "__all__"


class UploadImageSerializer(serializers.ModelSerializer):
    # applicant_id = TblApplicantProfileSerializer()

    class Meta:
        model = ApplicantPhoto
        fields = ('id', 'applicant_id', 'photo')
        read_only_fields = ('id',)
