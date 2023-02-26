from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, decorators, permissions, status
from rest_framework.decorators import api_view
from .serializers import *
from datetime import datetime

# Create your views here.

from rest_framework import routers, serializers, viewsets


class ApplicantDemographicsDetails(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        if request.data:
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
            _confirm = 0

            applicantprofile = TblAppProfile.objects.get(id=_userprofile)

            getDemographics = TblDemographicsDetails.objects.filter(
                app_year=_app_year, applicant=applicantprofile)

            _region_obj = TblRegions.objects.get(region_id=_region)

            _distric_obj = TblDistrict.objects.get(id=_distric)

            _domestic_region_obj = TblRegions.objects.get(region_id=_dom_region)

            _domestic_distric_obj = TblDistrict.objects.get(id=_dom_distric)

            iso_date_str = datetime.strptime(
                _dob, '%Y-%m-%d').date().isoformat()

            is_disabled = False
            if _disability == "true":
                is_disabled = True

            if getDemographics.exists():
                response_obj = {
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "Demographics Information Exists",
                }
                return Response(response_obj)
            else:

                created = TblDemographicsDetails.objects.create(
                    applicant=applicantprofile,
                    dob=datetime.fromisoformat(iso_date_str),
                    region=_region_obj,
                    distric=_distric_obj,
                    disability=is_disabled,
                    dom_region=_domestic_region_obj,
                    dom_distric=_domestic_distric_obj,
                    dom_postal=_dom_postal,
                    dom_ward=_dom_ward,
                    birth_cert_no=_birth_cert_no,
                    nationalIdNo=_nationalIdNo,
                    birthplace=_birthplace,
                    dom_village=_dom_village,
                    app_year=_app_year,
                    confirm=_confirm
                )
                response_obj = {
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "Demographics Information saved",
                }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                "message": "No request body params specified",

            }
            return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _app_year = request.GET.get('applicationYear')
        _userprofileId = request.GET.get('userProfileId')
        applicantprofile = TblAppProfile.objects.get(id=_userprofileId)

        getDemographics = TblDemographicsDetails.objects.filter(
            app_year=_app_year, applicant=applicantprofile).first()

        if getDemographics:
            demographicsSerializer = TblDemographicDetailsSerializer(
                instance=getDemographics)

            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Demographics Info Found",
                "data": demographicsSerializer.data
            }

            return Response(response_obj)
        else:
            response_obj = {
                "success": True,
                'status_code': status.HTTP_404_NOT_FOUND,
                "message": "Demographics notFound",
                "data": None
            }

            return Response(response_obj)

    def put(self, request, * args, **kwargs):
        _userprofileId = request.data['userProfileId']
        _app_year = request.data['applicationYear']
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
        _confirm = 0

        _region_obj = TblRegions.objects.get(region_id=_region)

        _distric_obj = TblDistrict.objects.get(id=_distric)

        _domestic_region_obj = TblRegions.objects.get(
            region_id=_dom_region)

        _domestic_distric_obj = TblDistrict.objects.get(id=_dom_distric)

        district_serializer = TblDemoRegionSerializer(instance=_distric)

        region_serializer = TblDemoRegionSerializer(instance=_region_obj)

        dom_region_serializer = TblDemoRegionSerializer(
            instance=_domestic_region_obj)

        dom_district_serializer = TblDemoRegionSerializer(
            instance=_domestic_distric_obj)

        iso_date_str = datetime.strptime(_dob, '%Y-%m-%d').date().isoformat()

        is_disabled = False
        if _disability == "true":
            is_disabled = True

        dataToEdit = {
            'dob':  iso_date_str,
            'region': region_serializer.data,
            'distric': district_serializer.data,
            'disability': is_disabled,
            'dom_region': dom_district_serializer.data,
            'dom_distric': dom_district_serializer.data,
            'dom_postal': _dom_postal,
            'dom_ward': _dom_ward,
            'birth_cert_no': _birth_cert_no,
            'nationalIdNo': _nationalIdNo,
            'birthplace': _birthplace,
            'dom_village': _dom_village,
            'confirm': _confirm
        }
        # applicantprofile = TblAppProfile.objects.get(id=_userprofileId)
        getDemographics = TblDemographicsDetails.objects.get(
            app_year=_app_year, applicant__id=_userprofileId, confirm=_confirm)
        demographicSerializer = TblDemographicDetailsSerializer(
            getDemographics, data=dataToEdit, partial=True)
      

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
                "message": demographicSerializer.errors,
            }
            return Response(response_obj)


class ConfirmDemographicsView(APIView):
    authentication_classes = []
    permission_classes = []

    def put(self, request, *args, **kwargs):
        _userprofileId = request.data['userProfileId']
        _app_year = request.data['applicationYear']
        _confirm = 0
        _confirmed = 1
        _applicant_profile = TblAppProfile.objects.get(
            id=_userprofileId
        )
        dataToConfirm = TblDemographicsDetails.objects.filter(
            applicant__applicant__app_year=_app_year, applicant=_applicant_profile, confirm=_confirm)
        if dataToConfirm.exists():
            _demographics_object = dataToConfirm[0]
            confirmDemographicSerializer = ConfirmDemographicSerializer(
                _demographics_object, data={'confirm': _confirmed}, partial=True)
            if confirmDemographicSerializer.is_valid():
                confirmDemographicSerializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Demographics Information Confirmed",
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "Invalid Input, Please try again",
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "already confirmed ",
            }
            return Response(response_obj)


class DemographicRegionViewSet(viewsets.ModelViewSet):
    queryset = TblRegions.objects.all()

    serializer_class = TblDemoRegionSerializer


class DemographicDistrictViewSet(viewsets.ModelViewSet):
    queryset = TblDistrict.objects.all()

    serializer_class = TblDemoDistrictSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        # Add some filtering based on query params
        _region_id = request.query_params.get('region', None)

        if _region_id is not None:
            queryset = queryset.filter(
                region_id=_region_id)

        # Paginate the results
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        response_obj = {
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "ok",
            'data': serializer.data
        }
        return Response(response_obj)
