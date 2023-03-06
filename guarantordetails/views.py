from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
# class  Choose guarntor type

# choose guarantor sex
class GuarantorDetailsLUGViewSet(viewsets.ModelViewSet):
    queryset = TBL_GuarantorDetailsLUG.objects.all()
    serializer_class = GuarantorDetailsLugSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        profile_id = request.data.get('profileId')
        app_year = request.data.get('app_year')
        if TBL_GuarantorDetailsLUG.objects.filter(applicant=profile_id, ay=app_year).exists():
            response_obj = {
                "success": False,
                "status": status.HTTP_208_ALREADY_REPORTED,
                "message": "Record already exists"
            }
            return Response(response_obj)
        else:
            data = {
                'applicant': profile_id,
                'first_name': request.data.get('firstName'),
                'sur_name': request.data.get('lastName'),
                'middle_name': request.data.get('MiddleName'),
                'sex': request.data.get('gender'),
                'region': request.data.get('region'),
                'district': request.data.get('district'),
                'postaladdress': request.data.get('postalAddress'),
                'mobile': request.data.get('mobile'),
                'email':request.data.get('email'),
                'ward': request.data.get('ward'),
                'village': request.data.get('village'),
                'idcardnumber': request.data.get('idCardNumber'),
                'cardtype': request.data.get('cardtype'),
                'photo': request.data.get('guarantorPhooto'),
                'ay': app_year
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "message": "PGD guarantor saved successfully",
                "data": serializer.data
            }
            return Response(response_obj)

    def update(self, request, *args, **kwargs):
        profile_id = request.data.get('profileId')
        app_year = request.data.get('app_year')
        instance = self.get_queryset().filter(applicant__profileId=profile_id, ay=app_year).first()
        if not instance:
            response_obj = {
                "success": False,
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Record does not exists"
            }
            return Response(response_obj)
        else:
            data = {
                'applicant': profile_id,
                'first_name': request.data.get('firstName'),
                'sur_name': request.data.get('lastName'),
                'middle_name': request.data.get('MiddleName'),
                'sex': request.data.get('gender'),
                'region': request.data.get('region'),
                'district': request.data.get('district'),
                'postaladdress': request.data.get('postalAddress'),
                'mobile': request.data.get('mobile'),
                'email': request.data.get('email'),
                'ward': request.data.get('ward'),
                'village': request.data.get('village'),
                'idcardnumber': request.data.get('idCardNumber'),
                'cardtype': request.data.get('cardtype'),
                'photo': request.data.get('guarantorPhooto'),
                'ay': app_year
            }
            serializer = self.get_serializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid:
                serializer.save()
                response_obj = {
                    "success": False,
                    "status": status.HTTP_200_OK,
                    "message": "Record does not exists",
                    "data": serializer.data
                }
                return Response(response_obj)
            else :
                response_obj = {
                    "success": False,
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Failed to update"
                }
                Response(response_obj)
class GuarantorDetailsPGDViewSet(viewsets.ModelViewSet):
    queryset = TBL_GuarantorDetailsPGD.objects.all()
    serializer_class = GuarantorDetailsLpgSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        profile_id = request.data.get('profileId')
        app_year = request.data.get('app_year')
        if TBL_GuarantorDetailsPGD.objects.filter(applicant_id=profile_id, ay=app_year).exists():
            response_obj ={
                "success": False,
                "status": status.HTTP_208_ALREADY_REPORTED,
                "message": "Record already exists"
            }
            return Response(response_obj)
        else:
            data = {
                'applicant': profile_id,
                'postaladdress': request.data.get('postalAddress'),
                'telephone': request.data.get('telephoneNo'),
                'contact_title': request.data.get('contactPersonTittle'),
                'inst': request.data.get('institution'),
                'district': request.data.get('district'),
                'contactperson': request.data.get('contactPersonNames'),
                'ay': app_year
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "message": "PGD guarantor saved successfully",
                "data" : serializer.data + headers
            }
            return Response(response_obj)

    def update(self, request, *args, **kwargs):
        profile_id = request.data.get('profileId')
        app_year = request.data.get('app_year')
        instance = self.get_queryset().filter(applicant__profileId=profile_id, ay=app_year).first()
        if not instance:
            response_obj = {
                "success": False,
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Record does not exists"
            }
            return Response(response_obj)
        else:
            data = {
                'applicant': profile_id,
                'postaladdress': request.data.get('postalAddress'),
                'telephone':request.data.get('telephoneNo'),
                'contact_title':request.data.get('contactPersonTittle'),
                'inst': request.data.get('institution'),
                'district':request.data.get('district'),
                'contactperson': request.data.get('contactPersonNames'),
                'ay': app_year,
            }
            serializer = self.get_serializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid:
                serializer.save()
                response_obj = {
                    "success": False,
                    "status": status.HTTP_200_OK,
                    "message": "Record does not exists",
                    "data": serializer.data
                }
                return Response(response_obj)
            else :
                response_obj = {
                    "success": False,
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Failed to update"
                }
                Response(response_obj)