
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import generics, decorators, permissions, status
from .external_api import CallExternalApi
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
            _necta_applicant = None
            if applicant_category == Constants.necta:
                _necta_applicant = TBL_App_NECTADetails.objects.filter(Q(index_no__exact=index_no) & Q(app_year__exact=app_year))
                if _necta_applicant.exists():
                    searchedApplicantSerializer= NectaApplicationSerializer(instance= _necta_applicant,many=True)
             
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
                            necta_applicant, created = TBL_App_NECTADetails.objects.get_or_create(
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
                            _necta_applicant_initial_category, created = TBL_App_ApplicantType.objects.get_or_create(
                                 necta = necta_applicant
                            )
                            # update the applicant details page
                            _necta_applicant_details, created = TBL_App_ApplicantDetails.objects.get_or_create(
                                applicant_categories=_necta_applicant_initial_category
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
    def post(self, request, format=None):
        if request.data:
            _center_name = request.data['center_name']
            _center_number = request.data['center_number']
            _index_no= request.data['index_no']
            _applcant_application_year = request.data['app_year']
            _exam_year = request.data['exam_year']
            applicant_school = TBL_App_ApplicantAttendedSchool.objects.filter(center_number=_center_number)
            applicant =TBL_App_NECTADetails.objects.get(index_no = _index_no, app_year=_applcant_application_year)
        
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

class ApplicantExistenceView(APIView): 
    """On applicnt confirms his details then check his existance"""

    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        if request.data:
            _index_no = request.data['index_no']
            _app_year =request.data['app_year']
            _applicant_category = request.data['applicant_type']

            if _applicant_category == Constants.necta:
                necta_applicant =get_object_or_404( TBL_App_NECTADetails, index_no = _index_no)

                _necta_applicant_initial_category, created = TBL_App_ApplicantType.objects.get_or_create(
                                 necta = necta_applicant
                            )
                          
                _necta_applicant_details, created = TBL_App_ApplicantDetails.objects.get_or_create(
                                applicant_categories=_necta_applicant_initial_category
                            )
                
                applicant = TBL_App_Applicant.objects.filter(
                     applicant_details =  _necta_applicant_details
                    )
                if applicant.exists():

                    response_obj={
                        "success": True,
                        'status_code': status.HTTP_200_OK,
                        "message":'exits',
                        "data": request.data
                        }
                    return Response(response_obj)
                else:
                    # updete the applicanrt model
                    response_obj={
                        "success": True,
                        'status_code': status.HTTP_200_OK,
                        "message":'updete_application_details',
                        "data": request.data
                        }
                    return Response(response_obj)

            else:
                # process the none nacta
                response_obj={
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "press none necata",
                
                }
                return Response(response_obj)
        response_obj={
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "No prameter or data specified in the request body",
            
            }
        return Response(response_obj)

class ApplicantDetailsView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        pass
    

    def post(self, request, format=None):
        if request.data:
            _index_no = request.data[ "index_no"]
            _app_year = request.data["app_year"]
            _applicant_type = request.data["applicant_type"]
            _applicant_category =request.data["applicant_category"]
            _phone_number = request.data["phone_number"]
            _email = request.data["email"]
            if  _applicant_type == Constants.necta:
                try:
                # check for applicant by index number and application year
                    necta_applicant =TBL_App_NECTADetails.objects.get( index_no = _index_no, app_year=_app_year)
                except necta_applicant.DoesNotExist:
                    raise
        
                # get or create the the applicant type if not exiting
                _necta_applicant_type, created = TBL_App_ApplicantType.objects.get_or_create(
                                        necta__index_no = necta_applicant.index_no
                                    )
                                
                # update the applicant details
                _necta_applicant_details = TBL_App_ApplicantDetails.objects.get(
                                        applicant_type__necta__index_no = _necta_applicant_type.necta.index_no,
                                    )
                _necta_applicant_details.phonenumber = _phone_number
                _necta_applicant_details.email = _email
                _necta_applicant_details.save()


                # create applicant categories
                application_category, create = TBL_App_Categories.objects.get_or_create(
                                name = _applicant_category
                        )
                # get or create the applicnt table if not  exits
                applicant, created = TBL_App_Applicant.objects.get_or_create(
                            applicant_details =  _necta_applicant_details,
                            application_category =application_category,
                        
                            )
                applicant_infos = TBL_App_Applicant.objects.filter(
                            applicant_details =  _necta_applicant_details,
                            application_category =application_category,
                        
                            )
                applicantSerializer=ApplicantSerializer(instance=  applicant_infos, many=True)

                response_obj = {
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": 'created or updated successifully',
                    "data": applicantSerializer.data
                    }
                return Response(response_obj)
            else:
                response_obj={
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": " process the none necta applicant",
                
                }
                return Response(response_obj)
        else:
            response_obj = {
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "No prameter or data specified in the request body",
            
            }
            return Response(response_obj)