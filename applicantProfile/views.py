from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, decorators, permissions, status
from .serializers import *
from loans_application.necta_serializers import UserProfileSerialiozer
from utils.rand_utils import RandUtils as rand_utilities
from rest_framework import routers, serializers, viewsets

from rest_framework import generics


class ApplicatProfileInfoView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None,):

        if request.data:
            _app_year = request.data['app_year']
            _index_no = request.data['index_no']
            return rand_utilities.getApplicantProfile(_index_no=_index_no, _app_year=_app_year)

        else:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                "message": "No parameter specified in the request body",
                'data': request.data
            }
            return Response(response_obj)


class UploadApplicantPhotoView(viewsets.ModelViewSet):

    queryset = ApplicantPhoto.objects.all()
    serializer_class = UploadImageSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Add some filtering based on query params
        _applicant_id = request.query_params.get('applicant_id', None)
        _is_confirmed = request.query_params.get('confirm', None)

        if _applicant_id is not None:
            queryset = queryset.filter(
                applicant_id=_applicant_id).first()

        # Paginate the results
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset,)

        response_obj = {
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "ok",
            'data': serializer.data
        }
        return Response(response_obj)
