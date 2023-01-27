
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from loans_application.none_serializers import NoneNectaApplicantSerializer
from .models import * 
from .necta_serializers import *
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import generics, decorators, permissions, status
from api_service.external_api import CallExternalApi
from utils.constants import Constants
from utils.serialize_models import SerializerManager
from utils.helpers import Helpers
from django.shortcuts import get_object_or_404
import json
from education_info.models import TBL_Education_ApplicantAttendedSchool
from education_info.serializers import *

class ApplicantTypeViewSet(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        if request.data:
            applicant_type = request.data['applicant_type']
            response_obj = {
                    'status_code': status.HTTP_200_OK,
                    'success': True,
                    'data': {
                    'applicant_cateory': applicant_type
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
            app_year = request.data['app_year']
            applicant_type =request.data['applicant_type']
            new_index_no = Helpers.get_new_index_no(index_no, exam_year)
            _necta_applicant = None
            if applicant_type == Constants.necta:
                _necta_applicant = TBL_App_NECTADetails.objects.filter(Q(index_no__exact=new_index_no) & Q(app_year__exact=app_year))
                if _necta_applicant.exists():
                    searchedApplicantSerializer = NectaApplicantSerializer(instance = _necta_applicant,many=True)
             
                    response_obj = {
                        'status_code': status.HTTP_200_OK,
                        "message": "Applicant exists, in pre-application  necta table check for an existence in-progress application table",
                        'success': True,
                        'data': {
                            "necta_index_no":index_no,
                            "new_index_no":new_index_no,
                            'applicant':searchedApplicantSerializer.data[0]}
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
                        new_index_no = Helpers.get_new_index_no(individual_data['particulars']['index_number'], exam_year) 
                        first_name = individual_data['particulars']['first_name']
                        middle_name = individual_data['particulars']['middle_name']
                        last_name = individual_data['particulars']['last_name']
                        middle_name = individual_data['particulars']['middle_name']
                       
                        education_level = ''
                        sex = ''
                        if  individual_data['particulars']['exam_id'] == 1:
                            education_level  = 'FORM_4'
                        else:
                            education_level  = 'FORM_6'
                        if individual_data['particulars']['sex'] == 'F':
                            sex = 'FEMALE'
                        else:
                            sex = 'MALE'

                        sur_name = ''
                        app_year = app_year
                        exam_year = exam_year
                        # in the front-end allow the user to confirm the his/her information
                        try:
                            necta_applicant, created = TBL_App_NECTADetails.objects.get_or_create(
                            index_no = new_index_no,
                            education_level =  education_level,
                            first_name = first_name,
                            middle_name =  middle_name ,
                            last_name= last_name,
                            sur_name =   sur_name,
                            sex = sex,
                            app_year =  app_year ,
                            exam_year = exam_year,
                            )
                            # update the category applicant instance
                            _necta_applicant_type, created = TBL_App_ApplicantType.objects.get_or_create(
                                 necta = necta_applicant
                            )
                            # update the applicant details page
                            _necta_applicant_details, created = TBL_App_ApplicantDetails.objects.get_or_create(
                                applicant_type=_necta_applicant_type
                            )

                        except IntegrityError as e: 
                            response_obj = {
                            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                            "success": False,
                            "message": f"{e}"}
                            return Response(response_obj)
                        response_obj = {
                            "success": True,
                            "status_code": status.HTTP_200_OK,
                            "message": "applicant, saved successfull",
                            "data": {
                                    'applicant_type': applicant_type,
                                    'new_index_no': new_index_no,
                                    'nacta_data':individual_data['particulars']
                            } }
                        return Response(response_obj) 
                           
                    else:
                        response_obj={
                            "success": True,
                            'status_code': status.HTTP_404_NOT_FOUND,
                                "data":individual_data }

                        return Response(response_obj)   
            
            else:
                #  the logic for the none necta user
                #  in  the early stages we use the original_no to search applicant exitance in the  none necta 
                #  but later after an application has completed, we provide the index_no for further reference 
                _none_necta_applicant, none_necta_created = TBL_App_NoneNECTADetails.objects.get_or_create(original_no=index_no, app_year=app_year)
                _searched_none_necta_applicant_serializer = NoneNectaApplicantSerializer(instance= _none_necta_applicant)
                if none_necta_created:
                    response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": "Created successifully",
                            'data':_searched_none_necta_applicant_serializer.data}
                    return Response(response_obj)
                else:
                    response_obj = {
                        'status_code': status.HTTP_200_OK,
                        "message": "Applicant exists, in pre-application  none table check for an existence in-progress application table",
                        'success': True,
                        'data': _searched_none_necta_applicant_serializer.data
                    }
                    return Response(response_obj)
        else:
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
            applicant_school, created = TBL_Education_ApplicantAttendedSchool.objects.get_or_create(center_number=_center_number)
            applicant =TBL_App_NECTADetails.objects.get(index_no = _index_no, app_year=_applcant_application_year)
            
        
            if created:
               
                if applicant_school.necta_applicants.filter(index_no = applicant.index_no).exists():
                    pass
                else:
                    applicant_school.center_name = _center_name
                    applicant_school.necta_applicants.add(applicant)
                    applicant_school.save()
                    s_serializer = SearchedNectaApplicationSerializer(instance=applicant_school)

                    response_obj={
               
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "added applicant information to school table",
                    "data": s_serializer.data
                    }
                    return Response(response_obj)
              
            else:
                if applicant_school:
                    applicant_school.center_name= _center_name
                    applicant_school.necta_applicants.add(applicant)
                    applicant_school.save()
                   
                    s_serializer = SearchedNectaApplicationSerializer(instance=applicant_school)

                    response_obj={
                        "success": True,
                        'status_code': status.HTTP_200_OK,
                        "message": "ok",
                        "data":s_serializer.data
                        }
                    return Response(response_obj)
                pass
        else:
            response_obj={
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "No prameter or data specified in the request body",
            
            }
            return Response(response_obj)

class ApplicantExistenceView(APIView): 
    """On applicnt confirms his/her details then check his existance"""

    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        if request.data:
            _index_no = request.data['index_no']
            _app_year =request.data['app_year']
            _applicant_category = request.data['applicant_type']

            if _applicant_category == Constants.necta:
               
                _necta_applicant =TBL_App_NECTADetails.objects.get(  index_no = _index_no, app_year= _app_year)

                _necta_applicant_type, created = TBL_App_ApplicantType.objects.get_or_create(
                                 necta = _necta_applicant
                            )
                          
                _necta_applicant_details, created = TBL_App_ApplicantDetails.objects.get_or_create(
                                applicant_type=_necta_applicant_type
                            )
                
                _necta_applicant = TBL_App_Applicant.objects.filter(
                     applicant_details =  _necta_applicant_details
                    )
            
                if _necta_applicant.exists():   
                   
                    app_d =TBL_App_Applicant.objects.get(
                     applicant_details =  _necta_applicant_details
                    )
            
                    d, c= TBL_App_PaymentDetails.objects.get_or_create(
                    applicant =app_d
                    )
                    applicant_all_details = PaymentSerializer(instance= d)

                    response_obj={
                        "success": True,
                        'status_code': status.HTTP_200_OK,
                        "message":'exits',
                        "data": applicant_all_details.data
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
                _none_necta_applicant =get_object_or_404( TBL_App_NoneNECTADetails,original_no = _index_no)

                _none_necta_applicant_initial_category, created = TBL_App_ApplicantType.objects.get_or_create(
                                 none_necta = _none_necta_applicant
                            )

                _none_necta_applicant_details, created = TBL_App_ApplicantDetails.objects.get_or_create(
                                applicant_type=_none_necta_applicant_initial_category
                            )
                _none_necta_applicant = TBL_App_Applicant.objects.filter(
                     applicant_details =  _none_necta_applicant_details
                    )

                if _none_necta_applicant.exists():

                    response_obj={
                        "success": True,
                        'status_code': status.HTTP_200_OK,
                        "message":'exists',
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

                
        response_obj={
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "No prameter or data specified in the request body",
            
            }
        return Response(response_obj)

class PreAplicantNectAContactInfosView(APIView):
    authentication_classes = []
    permission_classes = []
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
                except:
                    response_obj = {
                    "success": False,
                    'status_code': status.HTTP_404_NOT_FOUND,
                    "message": "No found",
                    
                    }
                    return Response(response_obj)
        
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

class PreAplicantNoneNectAContactInfosView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        if request.data:
            _index_no= request.data["index_no"]
            _applicant_type= request.data["applicant_type"]
            _first_name= request.data["first_name"]
            _middle_name= request.data["middle_name"]
            _last_name= request.data["last_name"]
            _app_year= request.data["app_year"]
            _exam_year= request.data["exam_year"]
            _sur_name= request.data["sur_name"]
            _sex= request.data["sex"]
            _applicant_category =request.data["applicant_category"]
            _phone_number = request.data["phone_number"]
            _email = request.data["email"]
            if  _applicant_type == Constants.none_necta:
                # Check the applicant with provided information 

                _new_sex_value = None

                if _sex == 'F':
                    _new_sex_value = 'FEMALE'
                else:
                    _new_sex_value = "MALE"
                
                try:
                    _none_necta_applicant =TBL_App_NoneNECTADetails.objects.get( original_no = _index_no, app_year=_app_year)
                
                    TBL_App_NoneNECTADetails.objects.filter(id = _none_necta_applicant.id).update( 
                    first_name = _first_name,
                    middle_name = _middle_name,
                    last_name = _last_name,
                    sex = _new_sex_value,
                    app_year = _app_year,
                    exam_year = _exam_year,
                    sur_name = _sur_name)
                except:
                    response_obj = {
                    "success": False,
                    'status_code': status.HTTP_404_NOT_FOUND,
                    "message": "No found",
                    
                    }
                    return Response(response_obj)
                _none_necta_applicant_type, created = TBL_App_ApplicantType.objects.get_or_create(
                                        none_necta__original_no = _none_necta_applicant.original_no
                                    )
                
                _none_necta_applicant_details = TBL_App_ApplicantDetails.objects.get(
                                        applicant_type__none_necta__original_no = _none_necta_applicant_type.none_necta.original_no,
                                    )

                _none_necta_applicant_details.phonenumber = _phone_number
                _none_necta_applicant_details.email = _email
                _none_necta_applicant_details.save()

                 # create applicant categories
                application_category, create = TBL_App_Categories.objects.get_or_create(
                                name = _applicant_category
                        )

                  # get or create the applicnt table if not  exits
                applicant, created = TBL_App_Applicant.objects.get_or_create(
                            applicant_details =  _none_necta_applicant_details,
                            application_category =application_category,
                        
                            )
                _applicant_infos = TBL_App_Applicant.objects.filter(
                            applicant_details =  _none_necta_applicant_details,
                            application_category =application_category,
                        
                            )
                _applicantSerializer=ApplicantSerializer(instance=  _applicant_infos, many=True)

                response_obj = {
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": 'created or updated successifully',
                    "data": _applicantSerializer.data
                    }
                return Response(response_obj)
            else:
                    
                response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "We intending to send a request for necta applicant?,if yes, try to change the applcant type",
                }
                return Response(response_obj)
        response_obj={
            "success": True,
            'status_code': status.HTTP_200_OK,
            "message": "No prameter or data specified in the request body",
            
            }
        return Response(response_obj)
class ChooseApploicantCategory(APIView):
    """check is Beneficiary?, if yes, is 25% paid?, if yes generate control_n0 for application fee
                                                if no generate controll number paying 25% for paying 25% """
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        _applicant_category = request.data['applicant_category']
        _index_no = request.data['index_no']
        _applicant_type = request.data['applicant_type']
        _app_year = request.data["app_year"]
        response  = CallExternalApi.applicant_loan_status(index_no=_index_no)
        parse_json = json.loads(response.text)

        if response.status_code == 200:
            match _applicant_category:

                case  Constants.PGD:
                    _request_body = Helpers.control_number_params(applicant_type=_applicant_type, index_no=_index_no, is_25_percent=False )
                    control_no_response  = CallExternalApi.request_control_number(request=json.dumps(_request_body).replace('/', r'\/'))
                    _parsed_json = json.loads(control_no_response.text)
                    if  control_no_response.status_code == 200:
                        _control_no_status = CallExternalApi.check_control_number_status(
                            billId=_parsed_json["billRequests"]["billId"]
                        )
                        payment_model= Helpers.update_payment_details(applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year, control_status_res=_control_no_status)
                        
                        applicant_all_details_serializer = PaymentSerializer(instance= payment_model  )
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'ok',
                            "data": applicant_all_details_serializer.data
                        
                            }
                        return Response(response_obj)
                    else: 
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'something went wrong',
                            "data": _parsed_json
                        
                            }
                        return Response(response_obj)
                    
                case  Constants.LUG:
                    if parse_json["lug"] is not None:
                        if parse_json['lug']["outstanding25Percent"] == 0:
                            _request_body = Helpers.control_number_params(applicant_type=_applicant_type, index_no=_index_no, is_25_percent=False )
                            control_no_response  = CallExternalApi.request_control_number(request=json.dumps(_request_body).replace('/', r'\/'))
                            # Helpers.Control_no_status(control_no_response=control_no_response, applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year)
                            _parsed_json = json.loads(control_no_response.text)
                            if  control_no_response.status_code == 200:
                                _control_no_status = CallExternalApi.check_control_number_status(
                                    billId=_parsed_json["billRequests"]["billId"]
                                )
                                payment_model= Helpers.update_payment_details(applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year, control_status_res=_control_no_status)
                               
                                applicant_all_details_serializer = PaymentSerializer(instance= payment_model  )
                                response_obj = {
                                    "success": True,
                                    'status_code': status.HTTP_200_OK,
                                    "message": 'ok',
                                    "data": applicant_all_details_serializer.data
                                
                                    }
                                return Response(response_obj)
                            else: 
                                response_obj = {
                                    "success": True,
                                    'status_code': status.HTTP_200_OK,
                                    "message": 'something went wrong',
                                    "data": _parsed_json
                                
                                    }
                                return Response(response_obj)
                           
                        else:
                            _request_body = Helpers.control_number_params(applicant_type=_applicant_type, index_no=_index_no, is_25_percent=True )

                            # generate control number
                            control_no_response  = CallExternalApi.request_control_number(request=json.dumps(_request_body).replace('/', r'\/'))

                            # check controll number status
                            # Helpers.Control_no_status(control_no_response=control_no_response, applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year)
                            _parsed_json = json.loads(control_no_response.text)
                            if  control_no_response.status_code == 200:
                                _control_no_status = CallExternalApi.check_control_number_status(
                                    billId=_parsed_json["billRequests"]["billId"]
                                )
                                payment_model= Helpers.update_payment_details(applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year, control_status_res=_control_no_status)
                               
                                applicant_all_details_serializer = PaymentSerializer(instance= payment_model  )
                                response_obj = {
                                    "success": True,
                                    'status_code': status.HTTP_200_OK,
                                    "message": 'ok',
                                    "data": applicant_all_details_serializer.data
                                
                                    }
                                return Response(response_obj)
                            else: 
                                response_obj = {
                                    "success": True,
                                    'status_code': status.HTTP_200_OK,
                                    "message": 'something went wrong',
                                    "data": _parsed_json
                                
                                    }
                                return Response(response_obj)

                           
                    else:
                        response_obj = {
                                    "success": True,
                                    'status_code': status.HTTP_200_OK,
                                    "message": 'ok',
                                   "data": parse_json 
                                    }
                        return Response(response_obj)

                case Constants.PGDL:
                    # check is Beneficiary? if yes generate control number for application fee payment
                    #                       if no display a message, " you must bbe Beneficiary"
                    _request_body = Helpers.control_number_params(applicant_type=_applicant_type, index_no=_index_no, is_25_percent=False )
                    control_no_response  = CallExternalApi.request_control_number(request=json.dumps(_request_body).replace('/', r'\/'))
                    # Helpers.Control_no_status(control_no_response=control_no_response, applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year)
                    _parsed_json = json.loads(control_no_response.text)
                    if  control_no_response.status_code == 200:
                        _control_no_status = CallExternalApi.check_control_number_status(
                            billId=_parsed_json["billRequests"]["billId"]
                        )
                        payment_model= Helpers.update_payment_details(applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year, control_status_res=_control_no_status)
                        
                        applicant_all_details_serializer = PaymentSerializer(instance= payment_model  )
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'ok',
                            "data": applicant_all_details_serializer.data
                        
                            }
                        return Response(response_obj)
                    else: 
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'something went wrong',
                            "data": _parsed_json
                        
                            }
                        return Response(response_obj)
                           
                    
        else:
            match _applicant_category:

                case  Constants.PGD:
                    _request_body = Helpers.control_number_params(applicant_type=_applicant_type, index_no=_index_no, is_25_percent=False )
                    control_no_response  = CallExternalApi.request_control_number(request=json.dumps(_request_body).replace('/', r'\/'))
                    _parsed_json = json.loads(control_no_response.text)
                    if  control_no_response.status_code == 200:
                        _control_no_status = CallExternalApi.check_control_number_status(
                            billId=_parsed_json["billRequests"]["billId"]
                        )
                        # payment_model= Helpers.update_payment_details(applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year, control_status_res=_control_no_status)
                        
                        applicant_all_details_serializer = PaymentSerializer(instance= payment_model  )
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'ok',
                            "data": applicant_all_details_serializer.data
                        
                            }
                        return Response(response_obj)
                    else: 
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'something went wrong',
                            "data": _parsed_json
                        
                            }
                        return Response(response_obj)
                    
                case  Constants.LUG:
                  
                    _request_body = Helpers.control_number_params(applicant_type=_applicant_type, index_no=_index_no, is_25_percent=False )
                    control_no_response  = CallExternalApi.request_control_number(request=json.dumps(_request_body).replace('/', r'\/'))
                    # Helpers.Control_no_status(control_no_response=control_no_response, applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year)
                    _parsed_json = json.loads(control_no_response.text)
                    if  control_no_response.status_code == 200:
                        _control_no_status = CallExternalApi.check_control_number_status(
                            billId=_parsed_json["billRequests"]["billId"]
                        )
                        payment_model= Helpers.update_payment_details(applicant_type=_applicant_type, index_no=_index_no, app_year=_app_year, control_status_res=_control_no_status)
                        
                        applicant_all_details_serializer = PaymentSerializer(instance= payment_model  )
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'ok',
                            "data": applicant_all_details_serializer.data
                        
                            }
                        return Response(response_obj)
                    else: 
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'something went wrong',
                            "data": _parsed_json
                        
                            }
                        return Response(response_obj)
                        
                case Constants.PGDL:
                   
                        response_obj = {
                            "success": True,
                            'status_code': status.HTTP_200_OK,
                            "message": 'You must Loan Beneficiary',
                            "data": _parsed_json
                        
                            }
                        return Response(response_obj)
                           
               

  