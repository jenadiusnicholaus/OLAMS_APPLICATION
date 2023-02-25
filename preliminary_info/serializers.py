from .models import *
from rest_framework import  serializers
class PreliminaryInforSerializer(serializers.ModelSerializer):
    class Meta:
        model =TblPreliminaryInfo
        fields ="__all__"
class ParentInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblParentsInfo
        fields ="__all__"

class DeathInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblParentDeathInfo
        fields = "__all__"
class DisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model =TblDisability
        fields = "__all__"
class DisabilityInforSerializer(serializers.ModelSerializer):
    class Meta:
        model =TblDisabilityInfo
        fields = "__all__"
class TasafInforSerializer(serializers.ModelSerializer):
    class Meta:
        model =TblTasafInfo
        fields = "__all__"
class ConfirmPreliminaryInfo(serializers.ModelSerializer):
    class Meta:
        model =TblPreliminaryInfo
        fields = 'confirm',