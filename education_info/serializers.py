
from .models import *
from rest_framework import serializers
from loans_application.none_necta_serializers import *
from loans_application.necta_serializers import *


class ApplicantSchoolInformationSerializer(serializers.ModelSerializer):
    necta_applicants = NectaApplicantSerializer(many=True)

    class Meta:
        model = TBL_Education_ApplicantAttendedSchool
        fields = "__all__"


class PostF4TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TblPost4EductionType
        fields = "__all__"


class SponsorsSerializers(serializers.ModelSerializer):

    class Meta:
        model = TblSponsorDetails
        fields = "__all__"


class DiplopmaInstitutionSerializers(serializers.ModelSerializer):

    class Meta:
        model = TblDiplomaInstitutions
        fields = "__all__"


class InstitutionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Institutions
        fields = "__all__"


class CoursesSerializers(serializers.ModelSerializer):

    class Meta:
        model = TblCourses
        fields = "__all__"


class EducationInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TBL_EducationInfo
        fields = "__all__"


class FormfourInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_Education_FormFourInfos
        fields = "__all__"


class FormsixInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBLEducationFormSixInfos
        fields = "__all__"


class DiplomaInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDiplomaDetails
        fields = "__all__"


class TertiaryEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_Education_TertiaryEducationInfos
        fields = "__all__"


class BachelorDegreeAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblTertiaryEducationBachelorAwards
        fields = "__all__"


class MasterDegreeAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblTertiaryEducationMasterAward
        fields = "__all__"


class ConfirmEducationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_EducationInfo
        fields = 'confirm',


class ConfirmTertiaryEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_Education_TertiaryEducationInfos
        fields = 'confirm',
