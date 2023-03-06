from rest_framework import serializers
from .models import *
class GuarantorDetailsLugSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_GuarantorDetailsLUG
        fields ="__all__"
class GuarantorDetailsLpgSerializer(serializers.ModelSerializer):
    class Meta:
        model =TBL_GuarantorDetailsPGD
        fields = "__all__"