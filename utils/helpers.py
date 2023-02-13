
from utils.constants import Constants
from loans_application.models import *
from rest_framework.response import Response
import json
from rest_framework import generics, decorators, permissions, status
from api_service.external_api import CallExternalApi
from education_info.models import *
from education_info.serializers import *


class Helpers:
    @staticmethod
    def get_new_index_no(index_no: str, exam_year):
        new_index_no = f"{index_no.replace('-', '.')}.{exam_year}"
        return new_index_no

    @staticmethod
    def control_number_params(applicant_type, index_no, is_25_percent):
        if applicant_type == Constants.necta:

            _necta_applicant_data = TBL_App_Applicant.objects.filter(
                applicant_details__applicant_type__necta__index_no=index_no).first()
            
           
            if  _necta_applicant_data is not None:
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

                return _request_body
        else:

            _none_necta_applicant_data = TBL_App_Applicant.objects.filter(
                applicant_details__applicant_type__none_necta__original_no=index_no).first()

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

            return _request_body

    @staticmethod
    def update_payment_details(applicant_type, index_no, control_no =None, app_year =None, control_status_res =None):

        ''' This a helper function to help on auto update the payments table when the payments found from the control number
        information endpoint.
        '''

       
        _referenceID = None
        _paid_when = None
        _used_by  = None
        _used_when = None
        _used_status = None
        _used_status = 0
        _updatedAt = timezone.now()
        if applicant_type == Constants.necta:
            
           

            if control_status_res is not None:
                _control_no = control_status_res['controlNo']

                _control_numner_infos_res = CallExternalApi.get_control_number_infos(
                _control_no)
            else:
                _control_numner_infos_res = CallExternalApi.get_control_number_infos(
                control_no)

            _jsonObj = json.loads(_control_numner_infos_res.text)
            try:
                payment_found = _jsonObj['paymentsFound']
            except:
                return None

            if payment_found:
                _payment_status = 1

                # TODO:
                # Update payments table for the payment_found 

                # _referenceID = _jsonObj['billRef']
                # _paid_when = _jsonObj['']
                # _amount_paid = _jsonObj['']
                # _used_by = _jsonObj['']
                # _used_when = _jsonObj['']
                # _used_status = _jsonObj['']
              
                
        
            else:
                _payment_status = 0
               

            TBL_App_PaymentDetails.objects.filter(
                applicant__applicant_details__applicant_type__necta__index_no=index_no,

            ).update(
                payment_status=_payment_status,
                control_number=_control_no,
                updated_at= _updatedAt
                
            )

            try:
                return TBL_App_PaymentDetails.objects.filter(
                    applicant__applicant_details__applicant_type__necta__index_no=index_no

                ).first()
            except:
                return None

        else:
            _payment_status = 0
            if control_status_res is not None:
                _control_no = control_status_res['controlNo']

                _control_numner_infos_res = CallExternalApi.get_control_number_infos(
                _control_no)
            else:
                _control_numner_infos_res = CallExternalApi.get_control_number_infos( control_no)
                _control_no = control_no

            _jsonObj = json.loads(_control_numner_infos_res.text)
            try:
                payment_found = _jsonObj['paymentsFound']
            except:
                return None

            if payment_found:
                _payment_status = 1

                # TODO:
                # Update payments table for the payment_found 

                # _referenceID = _jsonObj['billRef']
                # _paid_when = _jsonObj['']
                # _amount_paid = _jsonObj['']
                # _used_by = _jsonObj['']
                # _used_when = _jsonObj['']
                # _used_status = _jsonObj['']
                # _updatedAt = timezone.now

            else:
                _payment_status = 0
               


            TBL_App_PaymentDetails.objects.filter(
                applicant__applicant_details__applicant_type__none_necta__original_no=index_no,
            ).update(
                payment_status=_payment_status,
                control_number=_control_no,
                updated_at = _updatedAt
                
                )

            return TBL_App_PaymentDetails.objects.filter(
                applicant__applicant_details__applicant_type__none_necta__original_no=index_no

            ).first()

    @staticmethod
    def control_no_status(control_no_response, applicant_type, index_no, app_year):
        _parsed_json = json.loads(control_no_response.text)
        if control_no_response.status_code == 200:
            _control_no_status = CallExternalApi.check_control_number_status(
                billId=_parsed_json["billRequests"]["billId"]
            )
            Helpers.update_payment_details(
                applicant_type=applicant_type, index_no=index_no, app_year=app_year, control_status_res=_control_no_status)
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
                'status_code': status.HTTP_401_UNAUTHORIZED,
                "message": 'something went wrong',
                "data": _parsed_json

            }
            return Response(response_obj)

    def check_applicant_category(index_no,  app_year, applicant_type, applicant_category):
        a_c, c = TBL_App_Categories.objects.get_or_create(
            name=applicant_category
        )

        if applicant_type == Constants.necta:

            applicant = TBL_App_Applicant.objects.get(
                application_details__applicant_type__necta__index_no=index_no,
                application_details__applicant_type__necta_app_year=app_year
            )

            return applicant.application_category.name

        else:

            applicant = TBL_App_Applicant.objects.get(
                application_details__applicant_type__none_necta__index_no=index_no,
                application_details__applicant_type__none_necta_app_year=app_year
            )
            return str(applicant.application_category.name)

    def addSchool(center_name, center_number, index_no, necta_applicant):

        applicant_school, created = TBL_Education_ApplicantAttendedSchool.objects.get_or_create(
            center_number=center_number)

        if created:

            if applicant_school.necta_applicants.filter(index_no=necta_applicant.index_no).exists():
                pass

            else:
                applicant_school.center_name = center_name
                applicant_school.necta_applicants.add(necta_applicant)
                applicant_school.save()
               