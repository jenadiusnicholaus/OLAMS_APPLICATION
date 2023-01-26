
from utils.constants import Constants
from loans_application.models import *
from rest_framework.response import Response
import json
from rest_framework import generics, decorators, permissions, status
from api_service.external_api import CallExternalApi



class Helpers:
    @staticmethod
    def get_new_index_no(index_no: str, exam_year):
        new_index_no =  f"{index_no.replace('-', '.')}.{exam_year}"
        return new_index_no

    @staticmethod
    def control_number_params(applicant_type, index_no, is_25_percent):
        if applicant_type == Constants.necta:
        
            _necta_applicant_data = TBL_App_Applicant.objects.get(applicant_details__applicant_type__necta__index_no = index_no)
           
            _request_body = {
             "billAmount": 17075,
            "payerId": str(_necta_applicant_data.applicant_details.applicant_type.necta.index_no),
            "noOfExpirationDays": 5,
            "payerName": f"{_necta_applicant_data.applicant_details.applicant_type.necta.first_name}",
            "billDesc": "Control No Reuse",
            "billReqUser": f"{_necta_applicant_data.applicant_details.applicant_type.necta.first_name}",
            "payerPhone": f"{_necta_applicant_data.applicant_details.phonenumber}",
            "payerEmail": f"{_necta_applicant_data.applicant_details.email}",
            "paymentOption": 1,
            "billReference": f"{_necta_applicant_data.applicant_details.applicant_type.necta.index_no}-LOAN-25-REPAYMENT",
            "revenueSourceId": 1,
            "zoneId": 3,
            "indexNo": f"{_necta_applicant_data.applicant_details.applicant_type.necta.index_no}",
            "is25Percent": is_25_percent
            }
          
            return  _request_body
        else:
            
            _none_necta_applicant_data = TBL_App_Applicant.objects.get(applicant_details__applicant_type__none_necta__original_no = index_no)

            _request_body = {
             "billAmount": 17075,
            "payerId": str(_none_necta_applicant_data.applicant_details.applicant_type.none_necta.index_no),
            "noOfExpirationDays": 5,
            "payerName": f"{_none_necta_applicant_data.applicant_details.applicant_type.none_necta.first_name}",
            "billDesc": "Control No Reuse",
            "billReqUser": f"{_none_necta_applicant_data.applicant_details.applicant_type.none_necta.first_name}",
            "payerPhone": f"{_none_necta_applicant_data.applicant_details.phonenumber}",
            "payerEmail": f"{_none_necta_applicant_data.applicant_details.email}",
            "paymentOption": 1,
            "billReference": f"{_none_necta_applicant_data.applicant_details.applicant_type.none_necta.index_no}-LOAN-REPAYMENT",
            "revenueSourceId": 1,
            "zoneId": 3,
            "indexNo": f"{_none_necta_applicant_data.applicant_details.applicant_type.none_necta.index_no}",
            "is25Percent": is_25_percent
            }
            
            return  _request_body
    @staticmethod
    def update_payment_details(applicant_type, index_no, app_year,control_status_res):
        if applicant_type == Constants.necta:
            _payment_status = "not_paid"
            _control_no = control_status_res['controlNo']

            TBL_App_PaymentDetails.objects.filter(
                applicant__applicant_details__applicant_type__necta__index_no = index_no,
                applicant__applicant_details__applicant_type__necta__app_year =  app_year,

                ).update(
                    payment_status =  _payment_status,
                    control_number = _control_no,)
            
            return TBL_App_PaymentDetails.objects.get( 
                applicant__applicant_details__applicant_type__necta__index_no = index_no

                )
        else:
            _payment_status = "not_paid"
            _control_no = control_status_res['controlNo']
            TBL_App_PaymentDetails.objects.filter(
                applicant__applicant_details__applicant_type__none_necta__index_no = index_no,
                applicant__applicant_details__applicant_type__None_necta__app_year =  app_year,

                ).update(
                    payment_status =  _payment_status,
                    control_number = _control_no,)
            
            return TBL_App_PaymentDetails.objects.get( 
                applicant__applicant_details__applicant_type__none_necta__index_no = index_no

                )

    @staticmethod
    def Control_no_status(control_no_response, applicant_type, index_no, app_year):
        _parsed_json = json.loads(control_no_response.text)
        if  control_no_response.status_code == 200:
            _control_no_status = CallExternalApi.check_control_number_status(
                billId=_parsed_json["billRequests"]["billId"]
            )
            Helpers.update_payment_details(applicant_type=applicant_type, index_no=index_no, app_year=app_year, control_status_res=_control_no_status)
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": 'ok',
                "data": _control_no_status
            
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

    def updated_applicant_category(index_no,  app_year, applicant_type, applicant_category):
        a_c , c = TBL_App_Categories.objects.get_or_create(
                        name = applicant_category
                    )

        if applicant_type == Constants.necta:
           
            applicant = TBL_App_Applicant.objects.get(
                  application_details__applicant_type__necta__index_no = index_no,
                  application_details__applicant_type__necta_app_year=app_year
            )

            return applicant.application_category.name
            
        else:
             
            applicant = TBL_App_Applicant.objects.get(
                  application_details__applicant_type__none_necta__index_no = index_no,
                  application_details__applicant_type__none_necta_app_year=app_year
            )
            return str(applicant.application_category.name)
       






      
