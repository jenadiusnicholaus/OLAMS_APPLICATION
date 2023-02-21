from django.shortcuts import render
from education_info.models import *
from rest_framework.response import Response
from rest_framework import generics, decorators, permissions, status
from . serializers import *
from rest_framework.views import APIView



class CheckSchoolExistence(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **Kwargs):
        if request.data:
            _center_number = request.data['center_number']
            try:
                schoool = TBL_Education_ApplicantAttendedSchool.objects.get(center_number = _center_number)
                school_serializer = ApplicantSchoolInformationSerializer(instance=schoool)
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
class ApplicantEducationInformation(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):

        _profileId = request.data['profileId']
        _f4_no_of_seat =request.data['noOfSeat']
        _pst4ed =request.data['postFormFour']
        _f4sps = request.data['formFourSponsorship']
        _f4sps_cp = request.data['formFourSponsorContactPerson']
        _f4sps_cp_phone = request.data['formFourSponsorPhoneNo']
        _f4sps_cp_addr = request.data['formFourSponsorAddress']
        _pst4sps =request.data['postFormFourSponsorship']
        _pst4sps_cp = request.data['postFormFourContactPerson']
        _pst4sps_cp_phone = request.data['postFormFourSponsorPhoneNo']
        _pst4sps_cp_addr = request.data['postFormFourSponsorAddress']
        _ay = request.data['applicationYear']
        _confirm = False
        applicantprofile = TblAppProfile.objects.get(id=_profileId)
        educationInfo = TBL_EducationInfo.objects.filter(applicant=applicantprofile,ay=_ay)
        if educationInfo.exists():
            response_obj = {
                "success": False,
                'status_code': status.HTTP_200_OK,
                "message": "Education Information Exists",
            }
            return Response(response_obj)
        else:
            created = TBL_EducationInfo.objects.create(
                applicant =applicantprofile,
                f4_no_of_seat = _f4_no_of_seat,
                pst4ed = _pst4ed,
                f4sps = _f4sps,
                f4sps_cp=_f4sps_cp,
                f4sps_cp_phone=_f4sps_cp_phone,
                f4sps_cp_addr=_f4sps_cp_addr,
                pst4sps=_pst4sps,
                pst4sps_cp=_pst4sps_cp,
                pst4sps_cp_phone=_pst4sps_cp_phone,
                pst4sps_cp_addr=_pst4sps_cp_addr,
                ay=_ay,
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
    def get(self,request, *args,**kwargs):
        _profileId = request.data['profileId']
        _ay = request.data['applicationYear']
        #applicantprofile = TBL_App_Profile.objects.get(id=_profileId)
        educationInformation = TBL_EducationInfo.objects.get(applicant=_profileId, ay=_ay)
        educationInfoserializer = EducationInfoSerializer(instance=educationInformation)
        if educationInfoserializer is None:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_200_OK,
                "message": "You did not fill any education information for thia application year",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Demographics Info Found",
                "data": educationInfoserializer.data
            }
            return Response(response_obj)

    def put(self, request,*args, **kwargs):
        _ay = request.data['applicationYear']
        _profileId = request.data['profileId']
        _f4_no_of_seat = request.data['noOfSeat']
        _pst4ed = request.data['postFormFour']
        _f4sps = request.data['formFourSponsorship']
        _f4sps_cp = request.data['formFourSponsorContactPerson']
        _f4sps_cp_phone = request.data['formFourSponsorPhoneNo']
        _f4sps_cp_addr = request.data['formFourSponsorAddress']
        _pst4sps = request.data['postFormFourSponsorship']
        _pst4sps_cp = request.data['postFormFourContactPerson']
        _pst4sps_cp_phone = request.data['postFormFourSponsorPhoneNo']
        _pst4sps_cp_addr = request.data['postFormFourSponsorAddress']
        _confirm =0
        #applicantprofile = TblAppProfile.objects.get(id=_applicant)
        informationForEdit = TBL_EducationInfo.objects.filter(applicant=_profileId,ay=_ay,confirm=_confirm).first()
        if informationForEdit is not None:
            dataToEdit = {
                'confirm': _confirm,
                'f4_no_of_seat': _f4_no_of_seat,
                'pst4ed': _pst4ed,
                'f4sps': _f4sps,
                'f4sps_cp': _f4sps_cp,
                'f4sps_cp_phone': _f4sps_cp_phone,
                'f4sps_cp_addr': _f4sps_cp_addr,
                'pst4sps': _pst4sps,
                'pst4sps_cp': _pst4sps_cp,
                'pst4sps_cp_phone': _pst4sps_cp_phone,
                'pst4sps_cp_addr': _pst4sps_cp_addr
            }
            educationInforSerializer = EducationInfoSerializer(informationForEdit, data=dataToEdit, partial=True)
            if educationInforSerializer.is_valid():
                educationInforSerializer.save()
                response_obj ={
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
                "status_code": status.HTTP_200_OK,
                "message": "Education info Not Found"
            }
            return Response(response_obj)

class EducationConfirmation(APIView):
    authentication_classes = []
    permission_classes = []
    def put(self, request, *args,**kwargs):
        _applicant = request.data['f4indexno']
        _ay = request.data['applicationYear']
        _confirm = 0
        _confirmed =1
        dataToConfirm = TBL_EducationInfo.objects.filter(applicant=_applicant,ay=_ay,confirm=_confirm).first()
        if dataToConfirm is not None:
            confirmSerializer = ConfirmEducationInfoSerializer(dataToConfirm, data={'confirm': _confirmed}, partial=True)
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
