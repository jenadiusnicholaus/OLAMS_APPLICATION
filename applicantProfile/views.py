from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, decorators, permissions, status
from .serializers import *
from  loans_application.necta_serializers import UserProfileSerialiozer
from utils.rand_utils import RandUtils as rand_utilities
# Create your views here.

class ApplicatProfileInfo(APIView):
    authentication_classes = []
    permission_classes = []


    def post(self, request, format=None,):

        if request.data:
            _app_year = request.data['app_year']
            _index_no = request.data['index_no']
            return rand_utilities.getApplicantProfile(_index_no =_index_no, _app_year=_app_year)
         
        else:
            response_obj = {
                            "success": False,
                            'status_code': status.HTTP_400_BAD_REQUEST,
                            "message": "No parameter specified in the request body",
                            'data': request.data
                            }
            return Response(response_obj)
      
            



