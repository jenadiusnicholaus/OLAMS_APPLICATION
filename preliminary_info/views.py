import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
# Create your views here.
class PreliminaryInfoView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = TblPreliminaryInfo.objects.all()
    serializer_class = PreliminaryInforSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        # Map user input fields to object fields
        #applicantprofile = TblAppProfile.objects.get(id=request.data['profileId'])
        data = {
            'applicant': request.data.get('profileId'),
            'applicantDisable': request.data.get('applicant_disabled'),
            'fatherAlive': request.data.get('father_alive'),
            'motherAlive': request.data.get('mother_alive'),
            'resitFormFour': request.data.get('resit_form_4'),
            'formSixOrDiploma': request.data.get('form_6_or_diploma'),
            'fatherDisable': request.data.get('father_disabled'),
            'motherDisable': request.data.get('mother_disabled'),
            'tasafSponsored': request.data.get('tasaf_sponsored'),
            'hasGuardian': request.data.get('has_guardian'),
            'appYear': request.data.get('app_year'),
            'confirm':0,
        }
        serializer = PreliminaryInforSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Preliminary information Saved Successfully",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                "message": serializer.errors,
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        applicant = request.data.get('profileId')
        app_year = request.data.get('app_year')
        instance = TblParentsInfo.objects.get(applicant=applicant, appYear=app_year)
        # Map user input fields to object fields
        data = {
            'applicant': request.data.get('profileId', instance.applicant),
            'applicantDisable': request.data.get('applicant_disabled', instance.applicantDisable),
            'fatherAlive': request.data.get('father_alive', instance.fatherAlive),
            'motherAlive': request.data.get('mother_alive', instance.motherAlive),
            'resitFormFour': request.data.get('resit_form_4', instance.resitFormFour),
            'formSixOrDiploma': request.data.get('form_6_or_diploma', instance.formSixOrDiploma),
            'fatherDisable': request.data.get('father_disabled', instance.fatherDisable),
            'motherDisable': request.data.get('mother_disabled', instance.motherDisable),
            'tasafSponsored': request.data.get('tasaf_sponsored', instance.tasafSponsored),
            'hasGuardian': request.data.get('has_guardian', instance.hasGuardian),
            'appYear': request.data.get('app_year', instance.appYear),
            'confirm': 0,
        }
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid:
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Preliminary information Saved Successfully",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Preliminary information not available",
            }
            return Response(response_obj)
    

class ParentInfoView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = TblParentsInfo.objects.all()
    serializer_class = ParentInforSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    def create(self, request, *args, **kwargs):
        # Map user input fields to object fields
        # applicantprofile = TblAppProfile.objects.get(id=request.data['profileId'])
        data = {
            'applicant': request.data.get('profileId'),
            'firstName': request.data.get('firstName'),
            'middleName': request.data.get('middleName'),
            'lastName': request.data.get('lastName'),
            'occupation': request.data.get('ocupation'),
            'postalAddress':request.data.get('postalAddress'),
            'physicalAddress': request.data.get('physicalAddress'),
            'mobileNumber': request.data.get('mobileNo'),
            'gender': request.data.get('gender'),
            'applicantRelationship': request.data.get('relationShip'),
            'appYear': request.data.get('app_year'),
        }
        serializer = ParentInforSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Parent information Saved Successfully",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                "message": serializer.errors,
            }
            return Response(response_obj)

    def update(self, request, *args, **kwargs):
        applicant = request.data.get('profileId')
        app_year = request.data.get('app_year')
        instance = TblParentsInfo.objects.get(applicant=applicant, appYear=app_year)
        # Map user input fields to object fields
        data = {
            'applicant': request.data.get('profileId'),
            'firstName': request.data.get('firstName'),
            'middleName': request.data.get('middleName'),
            'lastName': request.data.get('lastName'),
            'occupation': request.data.get('ocupation'),
            'postalAddress': request.data.get('postalAddress'),
            'physicalAddress': request.data.get('physicalAddress'),
            'mobileNumber': request.data.get('mobileNo'),
            'gender': request.data.get('gender'),
            'applicantRelationship': request.data.get('relationShip'),
        }
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid:
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "parent information updated",
            }
            return Response(response_obj)
        else:
            response_obj ={
                "success":False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Parent information not available",
            }
            return Response(response_obj)
class ParentDeathInfoView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = TblParentsInfo.objects.all()
    serializer_class = DeathInformationSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    def create(self, request, *args, **kwargs):
        # Map user input fields to object fields
        # applicantprofile = TblAppProfile.objects.get(id=request.data['profileId'])
        data = {
            'applicant': request.data.get('profileId'),
            'deathCertificateNo': request.data.get('deathCertificateNo'),
            'deceasedName': request.data.get('deceasedName'),
            'applicantRelationship':request.data.get('applicantRelationship'),
            'appYear': request.data.get('app_year'),
        }
        serializer = DeathInformationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Death Information Saved Successfully",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                "message": serializer.errors,
            }
            return Response(response_obj)

    def update(self, request, *args, **kwargs):
        applicant = request.data.get('profileId')
        app_year = request.data.get('app_year')
        instance = TblParentDeathInfo.objects.get(applicant=applicant, appYear=app_year)
        # Map user input fields to object fields
        data = {
            'applicant': request.data.get('profileId'),
            'deathCertificateNo': request.data.get('deathCertificateNo'),
            'deceasedName': request.data.get('deceasedName'),
            'applicantRelationship': request.data.get('applicantRelationship'),
        }
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid:
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Parent Death information updated",
            }
            return Response(response_obj)
        else:
            response_obj ={
                "success":False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Parent Death information not available",
            }
            return Response(response_obj)
class DisabilityView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = TblDisability.objects.all()
    serializer_class = DisabilitySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    def create(self, request, *args, **kwargs):
        # Map user input fields to object fields
        # applicantprofile = TblAppProfile.objects.get(id=request.data['profileId'])
        data = {
            'name' : request.data.get('disabilityName'),
            'description': request.data.get('description')
        }
        serializer = DisabilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Disability Type Saved Successfully",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                "message": serializer.errors,
            }
            return Response(response_obj)

    def update(self, request, *args, **kwargs):
        DisabilityName = request.data.get('disabilityName')
        instance = TblDisability.objects.get(name=DisabilityName)
        # Map user input fields to object fields
        data = {
            'name': request.data.get('disabilityName'),
            'description': request.data.get('description')
        }
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid:
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Disability Name updated",
            }
            return Response(response_obj)
        else:
            response_obj ={
                "success":False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Disability Name not Found",
            }
            return Response(response_obj)
class ParentAndApplicantDisabilityInfoView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = TblDisabilityInfo.objects.all()
    serializer_class = DisabilityInforSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    def create(self, request, *args, **kwargs):
        # Map user input fields to object fields
        # applicantprofile = TblAppProfile.objects.get(id=request.data['profileId'])
        data = {
            'applicant': request.data.get('profileId'),
            'disabilityType': request.data.get('disabilityType'),
            'disabledPerson': request.data.get('disabilityType'),
            'appYear': request.data.get('app_year'),
        }
        serializer = DisabilityInforSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Disability Information Saved Successfully",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                "message": serializer.errors,
            }
            return Response(response_obj)

    def update(self, request, *args, **kwargs):
        applicant = request.data.get('profileId')
        app_year = request.data.get('app_year')
        instance = TblDisabilityInfo.objects.get(applicant=applicant, appYear=app_year)
        # Map user input fields to object fields
        data = {
            'applicant': request.data.get('profileId'),
            'disabilityType': request.data.get('disabilityType'),
            'disabledPerson': request.data.get('disabilityType'),
        }
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid:
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Disability information updated",
            }
            return Response(response_obj)
        else:
            response_obj ={
                "success":False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Disability information not available",
            }
            return Response(response_obj)

class TasafInfoView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = TblTasafInfo.objects.all()
    serializer_class = TasafInforSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    def create(self, request, *args, **kwargs):
        api_response = requests.get('http://api.example.com/data')

        # Check if the response is successful and non-empty
        if api_response.status_code == 200 and api_response.json():
            # Parse the API response and create a new TblTasafInfo instance
            api_data = api_response.json()
            tasaf_info = TblTasafInfo(
                applicant = request.data.get('profileId'),
                appYear = request.data.get('app_year'),
                firstName=api_data['first_name'],
                middleName=api_data['middle_name'],
                lastName=api_data['last_name'],
                dateOfBirth=api_data['date_of_birth'],
                registrationNo=api_data['registration_no'],
                memberLineNo=api_data['member_line_no'],
                gender=api_data['gender']
            )
            serializer = TasafInforSerializer(data=tasaf_info)
            if serializer.is_valid():
                serializer.save()
                response_obj = {
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "TASAF Information Saved Successfully",
                    "data": api_data
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    "message": serializer.errors,
                    "data":0
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                "message": api_response.status_code,
                "data": 0
            }
            return Response(response_obj)

    def update(self, request, *args, **kwargs):
        applicant = request.data.get('profileId')
        app_year = request.data.get('app_year')
        instance = TblTasafInfo.objects.get(applicant=applicant, appYear=app_year)
        # Map user input fields to object fields
        data = {
            'applicant': request.data.get('profileId'),
            'firstName' : request.data.get('firstName'),
            'middleName' : request.data.get('middleName'),
            'lastName' : request.data.get('lastName'),
            'dateOfBirth' : request.data.get('dateOfBirth'),
            'registrationNo' : request.data.get('registrationNo'),
            'memberLineNo' : request.data.get('memberLineNo'),
            'gender' : request.data.get('gender'),
        }
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid:
            serializer.save()
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "TASAF information updated",
            }
            return Response(response_obj)
        else:
            response_obj ={
                "success":False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Disability information not available",
            }
            return Response(response_obj)