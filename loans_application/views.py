
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from . models import *
from . serializers import *
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import generics, decorators, permissions, status
from . external_api import CallExternalApi
from utils.constants import Constants
from utils.serialize_models import SerializerManager
from django.shortcuts import get_object_or_404





class ApplicantCategoryViewSet(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        if request.data:
            applicant_categories = request.data['applicant_category']
            response_obj = {
                    'status_code': status.HTTP_200_OK,
                    'success': True,
                    'data': {
                    'applicant_cateory': applicant_categories,
                    }
                }
            return Response(response_obj)
        response_obj={
                    "success": True,
                    "message": "No data specied in the body"}
        return Response(response_obj)



class SearchNetaApplicantViewSet(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        if request.data:
            index_no = request.data['index_no']
            exam_year = request.data['exam_year']
            app_year = Constants.current_year
            applicant_category =request.data['applicant_cateory']
            applicant = None
            if applicant_category == Constants.necta:
                applicant = TBL_App_NECTADetails.objects.filter(Q(index_no__exact=index_no) & Q(app_year__exact=app_year))
                if applicant.exists():
                    searchedApplicantSerializer= NectaApplicationSerializer(instance= applicant,many=True)
             
                    response_obj = {
                        'status_code': status.HTTP_200_OK,
                        "message": "Applicant exists, Continue with the application",
                        'success': True,
                        'data': searchedApplicantSerializer.data[0]
                    }
                    return Response(response_obj)
                else:
                    try:
                        individual_data =  CallExternalApi.get_individual_necta_particulars(index_no=index_no, exam_year=exam_year)
                    except:
                        response_obj = {
                            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                            "success": False,
                            "message": "Somethng went wrong"}
                        return Response(response_obj)

                    if individual_data['status']['code'] != 0:
                        new_index_no = individual_data['particulars']['index_number']
                        first_name = individual_data['particulars']['first_name']
                        middle_name = individual_data['particulars']['middle_name']
                        last_name = individual_data['particulars']['last_name']
                        middle_name = individual_data['particulars']['middle_name']
                       
                        education_level = ''
                        sex =''
                        if  individual_data['particulars']['exam_id'] == 1:
                            education_level  = 'FORM_4'
                        else:
                            education_level  = 'FORM_6'
                        if individual_data['particulars']['sex'] == 'F':
                            sex = 'FEMALE'
                        else:
                            sex = 'MALE'

                        sur_name = ''
                        app_year = Constants.current_year
                        exam_year = exam_year
                        # in the front-end allow the user to confirm the his/her information
                        try:
                            applicant, created = TBL_App_NECTADetails.objects.get_or_create(
                            index_no = new_index_no,
                            education_level =  education_level ,
                            first_name = first_name,
                            middle_name =  middle_name ,
                            last_name= last_name,
                            sur_name =   sur_name,
                            sex = sex,
                            app_year =  app_year ,
                            exam_year = exam_year,
                            )
                            # update the category applicant instance
                            TBL_App_InitialApplicantCategory.objects.get_or_create(
                                 necta = applicant
                            )
                        
                        except IntegrityError as e: 
                            response_obj = {
                            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                            "success": False,
                            "message": f"{e}"}
                            return Response(response_obj)
                        response_obj={
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": "applicant, saved successfull",
                            "data": {
                                    'applicant_category': applicant_category,
                                    'nacta_data':individual_data['particulars']
                            } }
                        return Response(response_obj) 
                           
                    else:
                        response_obj={
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                                "data":individual_data }

                        return Response(response_obj)   
            
            else:
                #  the logic for the none necta user
                response_obj={
                        "success": True,
                        'status_code': status.HTTP_200_OK,
                        "message": "Process the none necta "}
                return Response(response_obj)

        response_obj={
                        "success": True,
                        'status_code': status.HTTP_200_OK,
                        "message": "No data specied in the body"}
        return Response(response_obj)

class AddSchoolView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        response_obj={
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "No data specied in the body",
                    "data": {}
                    }
        return Response(response_obj)
        
    def post(self, request, format=None):
        if request.data:
            _center_name = request.data['center_name']
            _center_number = request.data['center_number']
            _index_no= request.data['index_no']
            _applcant_application_year = request.data['app_year']
            _exam_year = request.data['exam_year']
    

            applicant_school = TBL_App_ApplicantAttendedSchool.objects.filter(center_number=_center_number)
        
            applicant = get_object_or_404(TBL_App_NECTADetails,index_no=_index_no)
        
            if applicant_school.exists:
               
                if applicant_school[0].necta_applicants.filter(
                    index_no= _index_no,
                    app_year =_applcant_application_year).exists():
                    pass
                else:
                    applicant_school[0].necta_applicants.add(applicant)
                    response_obj={
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "added applicant information to school table",
                    "data":request.data
                    }
                    return Response(response_obj)
                applicant_school[0].necta_applicants.add(applicant)
                response_obj= {
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "School exits",
                    "data":request.data
                    }
                return Response(response_obj)
            else:
                TBL_App_ApplicantAttendedSchool.objects.create(
                     necta_applicants = applicant,
                    center_number = _center_number,
                    center_name =_center_name,
                    )
                response_obj={
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "not exists",
                    "data":request.data
                    }
                return Response(response_obj)
        else:
            response_obj={
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "No prameter or data specified in the request body",
            
            }
            return Response(response_obj)




   
    
