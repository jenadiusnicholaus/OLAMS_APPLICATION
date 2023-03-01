from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializers import *
# Create your views here.
class PreliminaryInfoView(viewsets.ModelViewSet):
    queryset = TblPreliminaryInfo.objects.all()
    serializer_class = PreliminaryInforSerializer

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
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
        self.perform_update(serializer)
        return Response(serializer.data)
    


