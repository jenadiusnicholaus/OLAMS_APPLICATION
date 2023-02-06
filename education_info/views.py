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
                
