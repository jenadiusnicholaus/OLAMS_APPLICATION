from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, decorators, permissions, status
from .serializers import *
# Create your views here.
class ApplicatProfileInfo(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self,request,*args,**kwargs):
        _app_year = request.data['applicationYear']
        _f4indexNo = request.data['f4indexNo']
        if _f4indexNo.startwith('S') or _f4indexNo.startwith('P'):
            getApplicantProfileByYear = TBL_App_Profile.objects.filter(
                 applicant__applicant_details__applicant_type__necta__index_no__exact = _f4indexNo,
                 applicant__applicant_details__applicant_type__necta__app_year__exact = _app_year )
        else:
            pass



