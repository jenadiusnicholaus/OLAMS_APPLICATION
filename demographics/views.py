from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, decorators, permissions, status
from rest_framework.decorators import api_view
from .serializers import *
# Create your views here.
class ApplicantDemographicsDetails(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        _userprofile = request.data['userProfileId']
        _dob = request.data['dateOfBirth']
        _region = request.data['BirthRegionId']
        _distric = request.data['BirthDistrictId']
        _disability = request.data['disabilityStatus']
        _dom_region = request.data['curentRegion']
        _dom_distric = request.data['currentDistrict']
        _dom_postal = request.data['currentPostalAdress']
        _dom_ward = request.data['ward']
        _birth_cert_no = request.data['birthCertNo']
        # _cert_type_id = request.data['']
        _nationalIdNo = request.data['nidaIdNo']
        _birthplace = request.data['placeOfBirth']
        _dom_village = request.data['currentVillage']
        _app_year = request.data['applicationYear']
        _confirm =0
        getDemographics = TblDemographicsDetails.objects.filter(app_year=_app_year, applicant=_userprofile)
        if getDemographics.exists():
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Demographics Information Exists",
            }
            return Response(response_obj)
        else:
            created = TblDemographicsDetails.objects.create(
            applicant = _userprofile,
            dob = _dob,
            region= _region,
            distric= _distric,
            disability=_disability,
            dom_region= _dom_region,
            dom_distric= _dom_distric,
            dom_postal= _dom_postal,
            dom_ward= _dom_ward,
            birth_cert_no= _birth_cert_no,
            nationalIdNo= _nationalIdNo,
            birthplace= _birthplace,
            dom_village= _dom_village,
            app_year= _app_year,
            confirm= _confirm
        )
        return  Response(request.data)
    def get(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _userprofile = request.data['userProfileId']
        getDemographics = TblDemographicsDetails.objects.filter(app_year=_app_year, applicant=_userprofile).first()
        demographicsSerializer = TblDemographicDetailsSerializer(instance=getDemographics)
        response_obj = {
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "Demographics Info Found",
            "data": demographicsSerializer.data
        }
        return Response(response_obj)
    def put(self, request, * args, **kwargs):
        _userprofile = request.data['userProfileId']
        _app_year = request.data['applicationYear']
        _confirm = 0
        getDemographics = TblDemographicsDetails.objects.filter(app_year=_app_year, applicant=_userprofile,confirm=_confirm).first()
        demographicSerializer = TblDemographicDetailsSerializer(getDemographics,data=request.data)
        if demographicSerializer.is_valid():
            demographicSerializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Demographics Information Updated Successfully",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Demographics Information Not Updated",
            }
            return Response(response_obj)