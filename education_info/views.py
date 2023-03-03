from django.shortcuts import render
from education_info.models import *
from rest_framework.response import Response
from rest_framework import generics, decorators, permissions, status
from . serializers import *
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets
from applicantProfile.models import TblAppProfile
from loans_application.necta_serializers import UserProfileSerialiozer
from api_service. external_api import CallExternalApi
import json
from parse_jsons.necta_individual_particular_model import NectaResponse, Particulars, Status


class CheckSchoolExistence(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        if request.data:
            _center_number = request.data['center_number']
            try:
                schoool = TBL_Education_ApplicantAttendedSchool.objects.get(
                    center_number=_center_number)
                school_serializer = ApplicantSchoolInformationSerializer(
                    instance=schoool)
                response_obj = {
                    "success": False,
                    'status_code': status.HTTP_200_OK,
                    "message": "Found",
                    "data": school_serializer.data

                }
                return Response(response_obj)
            except:
                response_obj = {
                    "success": False,
                    'status_code': status.HTTP_404_NOT_FOUND,
                    "message": "No found",

                }
                return Response(response_obj)
        response_obj = {
            "success": False,
            'status_code': status.HTTP_400_BAD_REQUEST,
            "message": "No params sepecified",

        }
        return Response(response_obj)


class PostFormFourTypeViewSet(viewsets.ModelViewSet):
    queryset = TblPost4EductionType.objects.all()
    serializer_class = PostF4TypeSerializers


class ApplicantSponsorshipViewSet(viewsets.ModelViewSet):
    queryset = TblSponsorDetails.objects.all()
    serializer_class = SponsorsSerializers

    def get_serializer_class(self):
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        _sps_ed_type = request.data["sps_ed_type"]
        _user_profile_id = request.data["user_profile_id"]
        _app_year = request.data["app_year"]
        _sponsor_contact_person_full_name = request.data["sponsor_contact_person_full_name"]
        _sponsor_contact_person_phone_nunber = request.data["sponsor_contact_person_phone_nunber"]
        _sponsor_contact_person_address = request.data["sponsor_contact_person_address"]

        data = {
            "sponsored_ed_type": _sps_ed_type,
            "applicant": _user_profile_id,
            "sponsor_contact_person_full_name": _sponsor_contact_person_full_name,
            "sponsor_contact_person_phone_nunber": _sponsor_contact_person_phone_nunber,
            "sponsor_contact_person_address": _sponsor_contact_person_address,
            "app_year": _app_year

        }
        _spobj = TblSponsorDetails.objects.filter(

            app_year=_app_year, sponsored_ed_type=_sps_ed_type,  applicant__id=_user_profile_id)
        if _spobj.exists():
            sponsorsInformation = _spobj.first()
            serializer = SponsorsSerializers(instance=sponsorsInformation)

            response_obj = {
                "success": True,
                'status_code': status.HTTP_201_CREATED,
                "message": "Sponsor Information Found",
                "data": serializer.data,
            }
            return Response(response_obj)
        else:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response_obj = {
                "success": True,
                'status_code': status.HTTP_201_CREATED,
                "message": "Sponsor Information saved",
                "data": serializer.data,
            }
            headers = self.get_success_headers(serializer.data)
            return Response(response_obj,  headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_object(self):
        _sps_id = self.request.data["sps_id"]
        obj = TblSponsorDetails.objects.get(id=_sps_id)
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        _sps_ed_type = request.data["sps_ed_type"]
        _user_profile_id = request.data["user_profile_id"]
        _sponsor_contact_person_full_name = request.data["sponsor_contact_person_full_name"]
        _sponsor_contact_person_phone_nunber = request.data["sponsor_contact_person_phone_nunber"]
        _sponsor_contact_person_address = request.data["sponsor_contact_person_address"]

        data = {
            "sponsored_ed_type": _sps_ed_type,
            "sponsor_contact_person_full_name": _sponsor_contact_person_full_name,
            "sponsor_contact_person_phone_nunber": _sponsor_contact_person_phone_nunber,
            "sponsor_contact_person_address": _sponsor_contact_person_address

        }
        serializer = self.get_serializer(
            instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        response_obj = {
            "success": True,
            'status_code': status.HTTP_201_CREATED,
            "message": "Education Information saved",
            "data": serializer.data,
        }
        return Response(response_obj.  headers)

    def partial_update(self, request):
        pass


class ApplicantEducationInformationView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        _profileId = request.data['profile_id']
        _f4_no_of_seat = request.data['form_four_no_of_seat']
        _pst4ed = request.data['post_form_four_ed']
        _f4sps = request.data['form_four_sponsorship']
        _pst4sps = request.data['post_form_four_sponsorship']
        _app_year = request.data['app_year']

        _newf4sps = None
        _newPf4sps = None
        if _f4sps == "true":
            _newf4sps = 1 or True
        else:
            _newf4sps = 0 or False

        if _pst4sps == "true":
            _newPf4sps = 1 or True
        else:
            _newPf4sps = 0 or False

        _confirm = False
        applicantprofile = TblAppProfile.objects.get(id=_profileId)
        educationInfo = TBL_EducationInfo.objects.filter(
            applicant=applicantprofile, app_year=_app_year)
        _post_form_four_type = TblPost4EductionType.objects.get(
            id=_pst4ed,
        )

        if educationInfo.exists():
            response_obj = {
                "success": False,
                'status_code': status.HTTP_200_OK,
                "message": "Education Information Exists",
            }
            return Response(response_obj)
        else:
            created = TBL_EducationInfo.objects.create(
                applicant=applicantprofile,
                f4_no_of_seat=_f4_no_of_seat,
                pst4ed=_post_form_four_type,
                f4sps=_newf4sps,
                pst4sps=_newPf4sps,
                app_year=_app_year,
                confirm=_confirm,
            )
            if created:
                response_obj = {
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "Education Information Saved",
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    'status_code': status.HTTP_200_OK,
                    "message": "There is an error please try again",
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _profileId = request.GET.get('profileId')
        _ay = request.GET.get('applicationYear')
        # applicantprofile = TBL_App_Profile.objects.get(id=_profileId)
        educationInformation = TBL_EducationInfo.objects.get(
            applicant__id=_profileId, app_year=_ay)
        educationInfoserializer = EducationInfoSerializer(
            instance=educationInformation)
        if educationInfoserializer is None:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_204_NO_CONTENT,
                "message": "You did not fill any education information for thia application year",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Education Info Found",
                "data": educationInfoserializer.data
            }
            return Response(response_obj)

    def get_object(self):
        _confirm = 0
        _profileId = self.request.data['profile_id']
        _ed_info_id = self.request.data['ed_info_id']
        _app_year = self.request.data['app_year']
        obj = TBL_EducationInfo.objects.filter(id=_ed_info_id,
                                               applicant__id=_profileId, app_year=_app_year, confirm=_confirm).first()
        return obj

    def put(self, request, *args, **kwargs):

        _f4_no_of_seat = request.data['form_four_no_of_seat']
        _pst4ed = request.data['post_form_four_ed']
        _f4sps = request.data['form_four_sponsorship']
        _pst4sps = request.data['post_form_four_sponsorship']
        _confirm = 0

        instance = self. get_object()
        if instance is not None:
            dataToEdit = {
                'confirm': _confirm,
                'f4_no_of_seat': _f4_no_of_seat,
                'pst4ed': _pst4ed,
                'f4sps': _f4sps,
                'pst4sps': _pst4sps,

            }
            educationInforSerializer = EducationInfoSerializer(
                instance, data=dataToEdit, partial=True)
            if educationInforSerializer.is_valid():
                educationInforSerializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education information Updated Successfully",
                    'data': educationInforSerializer.data
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Education info Not Found"
            }
            return Response(response_obj)


class FormFourDetailsView(APIView):  # Other form four seating's Details
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        _second_seat_index_no = request.data['otherFormFourIndexno']
        _third_seat_index_no = request.data['otherFormFourIndexno2']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        formFourDetails = TBL_Education_FormFourInfos.objects.filter(
            app_year=_app_year, applicant=_applicant).first()
        if formFourDetails is not None:
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Form four Details Updated successfully"
            }
            return Response(response_obj)
        else:
            created = TBL_Education_FormFourInfos.objects.create(
                applicant=applicantprofile,
                app_year=_app_year,
                second_seat_index_no=_second_seat_index_no,
                third_seat_index_no=_third_seat_index_no,
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Other form four seats saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        formFourDetails = TBL_Education_FormFourInfos.objects.get(
            app_year=_app_year, applicant=_applicant)
        formFourSerializer = FormfourInformationSerializer(
            instance=formFourDetails)
        if formFourSerializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": formFourSerializer.data,
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no other form four seating"
            }
            return Response(response_obj)

    def get_object(self):
        _applicant = self.request.data['profileId']
        _app_year = self.request.data['applicationYear']
        _form_four_info_id = self.request.data['form_four_info_id']
        obj = TBL_Education_FormFourInfos.objects.filter(id=_form_four_info_id,
                                                         applicant=_applicant, app_year=_app_year).first()
        return obj

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        _second_seat_index_no = request.data['otherFormFourIndexno']
        _third_seat_index_no = request.data['otherFormFourIndexno2']
        instance = self.get_object()
        if instance is not None:
            dataToEdit = {
                'second_seat_index_no': _second_seat_index_no,
                'third_seat_index_no': _third_seat_index_no,
            }
            form4detailserializer = FormfourInformationSerializer(
                instance, data=dataToEdit, partial=True)
            if form4detailserializer.is_valid():
                form4detailserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Education info Not Found"
            }
            return Response(response_obj)


class FormSixDetailsView(APIView):  # FORM SIX DETAILS #####################
    authentication_classes = []
    permission_classes = []

    def get_user_profile(self):
        try:
            profile = TblAppProfile.objects.get(
                id=self.request.data['profileId'])
            return profile
        except TblAppProfile.objects.DoesNotExists as e:
            raise e

    def search_form_6_details(self, app_year, applicant_id):
        formSixDetails = TBLEducationFormSixInfos.objects.filter(
            app_year=app_year, applicant__id=applicant_id)
        return formSixDetails

    def get_object(self, app_year, applicant_id, form_6_info_id=None):
        obj = TBLEducationFormSixInfos.objects.get(
            app_year=app_year, applicant=applicant_id, )
        return obj

    def post(self, request, *args, **kwargs):
        _applicant = self.request.data['profileId']
        _app_year = request.data['applicationYear']

        _f6index_no = request.data['f6Indexno']

        if self.search_form_6_details(_app_year, _applicant).exists():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "Form six information already exits for this year."
            }
            return Response(response_obj)
        else:

            _index_components = _f6index_no.split("-")
            _prefix_index_number = f"{_index_components[0]}-{_index_components[1]}"
            _sufix_index_number = _index_components[2]

            _response = CallExternalApi.get_individual_necta_particulars(
                index_no=_prefix_index_number, exam_year=_sufix_index_number)

            _response = CallExternalApi.get_individual_necta_particulars(
                index_no=_prefix_index_number, exam_year=_sufix_index_number)

            _particulars = Particulars(**_response['particulars'])

            _status = Status(**_response['status'])
            _student = NectaResponse(_particulars, status)

            if _student.status.code == 200 and _student.particulars.center_number:
                created = TBLEducationFormSixInfos.objects.create(
                    applicant=self.get_user_profile(),
                    app_year=_app_year,
                    f6index_no=_f6index_no,
                )
                if created:

                    response_obj = {
                        "success": True,
                        "status_code": status.HTTP_200_OK,
                        "message": "Form six details saved Successfully"
                    }
                    return Response(response_obj)
            else:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form six index no is no valid please double check it. and try again"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']

        formsixserializer = FormsixInformationSerializer(
            instance=self.get_object(_app_year, _applicant))

        if formsixserializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": formsixserializer.data,
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no form six details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        _f6index_no = request.data['f6Indexno']
        informationForEdit = TBLEducationFormSixInfos.objects.filter(applicant=_applicant,
                                                                     app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                'f6index_no': _f6index_no,
            }
            form6detailserializer = FormsixInformationSerializer(
                informationForEdit, data=dataToEdit, partial=True)
            if form6detailserializer.is_valid():
                form6detailserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form six information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form six info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Form six info Not Found"
            }
            return Response(response_obj)


class DiplomaInstitutesViewSet(viewsets.ModelViewSet):
    queryset = TblDiplomaInstitutions.objects.all()
    serializer_class = DiplopmaInstitutionSerializers


class TertiaryInstitutesViewSet(viewsets.ModelViewSet):
    queryset = Institutions.objects.all()
    serializer_class = InstitutionSerializers


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = TblCourses.objects.all()
    serializer_class = CoursesSerializers


class DiplomaDetailsView(APIView):
    authentication_classes = []
    permission_classes = []

    def get_institute_object(self, diplomaInstitution):
        obj = TblDiplomaInstitutions.objects.get(id=diplomaInstitution,)
        return obj

    def post(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _applicant = request.data['profileId']
        _diplomaInstitution = request.data['diplomaInstitution']
        _avn = request.data['avn']
        _entryYear = request.data['entryYear']
        _graduateYear = request.data['graduatedYear']
        _gpa = request.data['gpa']
        _registrationNumber = request.data['registrationNo']
        _applicantprofile = TblAppProfile.objects.get(id=_applicant)
        _diplomadetails = TblDiplomaDetails.objects.filter(
            app_year=_app_year, applicant=_applicant)
        if _diplomadetails.exists():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "Diploma Details already exist for this year"
            }
            return Response(response_obj)
        else:
            created = TblDiplomaDetails.objects.create(
                applicant=_applicantprofile,
                app_year=_app_year,
                diplomaInstitution=self.get_institute_object(
                    diplomaInstitution=_diplomaInstitution),
                avn=_avn,
                entryYear=_entryYear,
                graduateYear=_graduateYear,
                gpa=_gpa,
                registrationNumber=_registrationNumber
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form Diploma details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        diplodetails = TblDiplomaDetails.objects.get(
            app_year=_app_year, applicant=_applicant)
        diplodetailserializer = DiplomaInformationSerializer(
            instance=diplodetails)
        if diplodetailserializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": diplodetailserializer.data,
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no diploma details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _applicant = request.data['profileId']
        _diplomaInstitution = request.data['diplomaInstitution']
        _avn = request.data['avn']
        _entryYear = request.data['entryYear']
        _graduateYear = request.data['graduatedYear']
        _gpa = request.data['gpa']
        _registrationNumber = request.data['registrationNo']
        informationForEdit = TblDiplomaDetails.objects.filter(applicant=_applicant,
                                                              app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                'diplomaInstitution': _diplomaInstitution,
                'avn': _avn,
                'entryYear': _entryYear,
                'graduateYear': _graduateYear,
                'gpa': _gpa,
                'registrationNumber': _registrationNumber,
            }
            form6detailserializer = FormsixInformationSerializer(
                informationForEdit, data=dataToEdit, partial=True)
            if form6detailserializer.is_valid():
                form6detailserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Diploma information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form Diploma info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Diploma info Not Found"
            }
            return Response(response_obj)


class TertiaryEducationView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        _applicationYear = request.data['applicationYear']
        _applicant = request.data['profileId']
        _admittedInstitute = request.data['admittedInst']
        _admittedCourse = request.data['admittedCourse']
        _admittedDegreeCategory = request.data['admittedDegree']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        institutionadmitted = Institutions.objects.get(id=_admittedInstitute)
        courseadmitted = TblCourses.objects.get(id=_admittedCourse)
        tertiaryinfo = TBL_Education_TertiaryEducationInfos.objects.filter(applicant=_applicant,
                                                                           applicationYear=_applicationYear)
        if tertiaryinfo.exists():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "Tertiary Education Details already exist for this year"
            }
            return Response(response_obj)
        else:
            created = TBL_Education_TertiaryEducationInfos.objects.create(
                applicationYear=_applicationYear,
                applicant=applicantprofile,
                admittedInstitute=institutionadmitted,
                admittedCourse=courseadmitted,
                admittedDegreeCategory=_admittedDegreeCategory,
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Tertiary details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _applicationYear = request.data['applicationYear']
        _applicant = request.data['profileId']
        tertiaryInfo = TBL_Education_TertiaryEducationInfos.objects.get(
            applicationYear=_applicationYear, applicant=_applicant)
        tertiaryInfoSerializer = TertiaryEducationSerializer(
            instance=tertiaryInfo)
        if tertiaryInfoSerializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": tertiaryInfoSerializer.data,
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no Tertiary education details for this year"
            }
            return Response(response_obj)

    def get_object(self):
        obj = TBL_Education_TertiaryEducationInfos.objects.filter(applicant=self.request.data['profileId'],
                                                                  applicationYear=self.request.data['applicationYear']).first()
        return obj

    def put(self, request, *args, **kwargs):
        _applicationYear = request.data['applicationYear']
        _applicant = request.data['profileId']
        _admittedInstitute = request.data['admittedInst']
        _admittedCourse = request.data['admittedCourse']
        _admittedDegreeCategory = request.data['admittedDegree']
        institutionadmitted = Institutions.objects.get(id=_admittedInstitute)
        courseadmitted = TblCourses.objects.get(id=_admittedCourse)
        informationForEdit = self.get_object()
        if informationForEdit is not None:
            dataToEdit = {
                'admittedInstitute': institutionadmitted,
                'admittedCourse': courseadmitted,
                'admittedDegreeCategory': _admittedDegreeCategory,
            }
            tertiaryInforSerializer = TertiaryEducationSerializer(
                informationForEdit, data=dataToEdit, partial=True)
            if tertiaryInforSerializer.is_valid():
                tertiaryInforSerializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Tertiary information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Tertiary info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Tertiary info Not Found"
            }
            return Response(response_obj)


# BACHELOR DEGREE AWARD DETAILS FOR PGD ##############
class TertiaryEducationBachelorAwardsView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _award = request.data['award']
        _regno = request.data['regno']
        _entryYear = request.data['entryYear']
        _graduateYear = request.data['graduateYear']
        _gpa = request.data['gpa']
        _app_year = request.data['applicationYear']
        _institution = request.data['institutionGraduated']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        awardedinstitution = Institutions.objects.get(id=_institution)
        bachelorAward = TblTertiaryEducationBachelorAwards.objects.filter(applicant=_applicant,
                                                                          applicationYear=_institution)
        if bachelorAward.exist():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "This Award already exist for this year"
            }
            return Response(response_obj)
        else:
            created = TblTertiaryEducationBachelorAwards.objects.create(
                applicant=applicantprofile,
                award=_award,
                regno=_regno,
                entryYear=_entryYear,
                graduateYear=_graduateYear,
                gpa=_gpa,
                app_year=_app_year,
                institution=awardedinstitution
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Tertiary details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _applicant = request.data['profileId']
        bachelorAwards = TblTertiaryEducationBachelorAwards.objects.get(applicationYear=_app_year,
                                                                        applicant=_applicant)
        bachelorawardserializer = BachelorDegreeAwardSerializer(
            instance=bachelorAwards)
        if bachelorawardserializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": bachelorawardserializer.data,
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no Bachelor degree details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _award = request.data['award']
        _regno = request.data['regno']
        _entryYear = request.data['entryYear']
        _graduateYear = request.data['graduateYear']
        _gpa = request.data['gpa']
        _app_year = request.data['applicationYear']
        _institution = request.data['institutionGraduated']
        awardedinstitution = Institutions.objects.get(id=_institution)
        informationForEdit = TblTertiaryEducationBachelorAwards.objects.filter(applicant=_applicant,
                                                                               app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                "award": _award,
                "regno": _regno,
                "entryYear": _entryYear,
                "graduateYear": _graduateYear,
                "gpa": _gpa,
                "institution": awardedinstitution
            }
            bachelorawardserializer = BachelorDegreeAwardSerializer(
                informationForEdit, data=dataToEdit, partial=True)
            if bachelorawardserializer.is_valid():
                bachelorawardserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Bachelor degree award Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Bachelor degree info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Bachelor degree info Not Found"
            }
            return Response(response_obj)


# MASTER DEGREE AWARD DETAILS FOR PGD  ###########
class MasterDegreeAwardView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _master_award = request.data['masterAward']
        _regNo = request.data['masterRegNo']
        _entryYear = request.data['masterEntryYear']
        _graduateYear = request.data['masterGraduateYear']
        _gpa = request.data['masterGpa']
        _app_year = request.data['applicationYear']
        _institution = request.data['institutionGraduated']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        awardedinstitution = Institutions.objects.get(id=_institution)
        masterAward = TblTertiaryEducationMasterAward.objects.filter(applicant=_applicant,
                                                                     applicationYear=_institution)
        if masterAward.exist():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "This Award already exist for this year"
            }
            return Response(response_obj)
        else:
            created = TblTertiaryEducationMasterAward.objects.create(
                applicant=applicantprofile,
                master_award=_master_award,
                regNo=_regNo,
                entryYear=_entryYear,
                graduateYear=_graduateYear,
                gpa=_gpa,
                app_year=_app_year,
                institution=awardedinstitution
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Master details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _applicant = request.data['profileId']
        masterAwards = TblTertiaryEducationMasterAward.objects.get(applicationYear=_app_year,
                                                                   applicant=_applicant)
        masterrawardserializer = MasterDegreeAwardSerializer(
            instance=masterAwards)
        if masterrawardserializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": masterrawardserializer.data,
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no Master degree details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _master_award = request.data['masterAward']
        _regNo = request.data['masterRegNo']
        _entryYear = request.data['masterEntryYear']
        _graduateYear = request.data['masterGraduateYear']
        _gpa = request.data['masterGpa']
        _app_year = request.data['applicationYear']
        _institution = request.data['institutionGraduated']
        awardedinstitution = Institutions.objects.get(id=_institution)
        informationForEdit = TblTertiaryEducationMasterAward.objects.filter(applicant=_applicant,
                                                                            app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                "master_award": _master_award,
                "regNo": _regNo,
                "entryYear": _entryYear,
                "graduateYear": _graduateYear,
                "gpa": _gpa,
                "institution": awardedinstitution
            }
            masterawardserializer = MasterDegreeAwardSerializer(
                informationForEdit, data=dataToEdit, partial=True)
            if masterawardserializer.is_valid():
                masterawardserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Master degree award Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Master degree info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Master degree info Not Found"
            }
            return Response(response_obj)


# CONFIRM EDUCATION INFORMATION ################
class EducationConfirmation(APIView):
    authentication_classes = []
    permission_classes = []

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _ay = request.data['applicationYear']
        _confirm = 0
        _confirmed = 1
        dataToConfirm = TBL_EducationInfo.objects.filter(
            applicant=_applicant, ay=_ay, confirm=_confirm).first()
        if dataToConfirm is not None:
            confirmSerializer = ConfirmEducationInfoSerializer(
                dataToConfirm, data={'confirm': _confirmed}, partial=True)
            if confirmSerializer.is_valid():
                confirmSerializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education information Confirmed Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "There is an error on Confirm Education Information"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "No matching education information found"
            }
            return Response(response_obj)


class TertiaryEducationConfirmation(APIView):
    authentication_classes = []
    permission_classes = []

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _applicationYear = request.data['applicationYear']
        _confirm = 0
        _confirmed = 1
        dataToConfirm = TBL_Education_TertiaryEducationInfos.objects.filter(
            applicant=_applicant, applicationYear=_applicationYear, confirm=_confirm).first()
        if dataToConfirm is not None:
            confirmSerializer = ConfirmTertiaryEducationSerializer(
                dataToConfirm, data={'confirm': _confirmed}, partial=True)
            if confirmSerializer.is_valid():
                confirmSerializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": " Tertiary Education information Confirmed Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "There is an error on Confirm Tertiary Education Information"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "No matching Tertiary education information found"
            }
            # Add some filtering based on query params
            return Response(response_obj)
