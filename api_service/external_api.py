import requests
import json
from utils.constants import Constants
from api_service.apis import Api

class CallExternalApi:
    @staticmethod
    def getparems(index_no, exam_year, exam_id, api_key ):
        payload = json.dumps({
        "index_number": index_no,
        "exam_year":exam_year,
        "exam_id": exam_id,
        "api_key": api_key
        })
        return payload


    @staticmethod
    def get_individual_necta_particulars( index_no,exam_year ):
        exam_id = Constants.form_four_axam_id
        api_key = Constants.api_key
        url = Api.URLS.NECTA_APPLICANT_INFORMATION_BASE_URL
    
        payload = CallExternalApi.getparems(
            index_no=index_no,exam_year=exam_year,
            exam_id=exam_id, api_key=api_key)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request(Api.Methods.POST, url, headers=headers, data=payload)

        json_data = json.loads(response.text )
    
        return json_data

    @staticmethod
    def applicant_loan_status(index_no):
        url = f"{ Api.URLS.BENFICIARY_OR_25_PERCENT_BASE_URL}?indexNo={index_no}"
        response = requests.request(Api.Methods.GET, url)
        return response

    @staticmethod
    def request_control_number(request):
        _my_request = json.loads(request)
        _billAmount = _my_request["billAmount"]
        _payerId = _my_request["payerId"]
        _noOfExpirationDays = _my_request["noOfExpirationDays"]
        _payerName = _my_request["payerName"]
        _billDesc = _my_request["billDesc"]
        _billReqUser = _my_request["billReqUser"]
        _payerPhone = _my_request["payerPhone"]
        _payerEmail = _my_request["payerEmail"]
        _paymentOption = _my_request["paymentOption"]
        _billReference = _my_request["billReference"]
        _revenueSourceId = _my_request["revenueSourceId"]
        _zoneId = _my_request["zoneId"]
        _indexNo = _my_request["indexNo"]
        _is25Percent = _my_request["is25Percent"]


        url = Api.URLS.CONTROL_NUMBER_BASE_URL

        payload = json.dumps({
            "billAmount": _billAmount,
            "payerId": _payerId,
            "noOfExpirationDays":_noOfExpirationDays,
            "payerName": _payerName,
            "billDesc": _billDesc,
            "billReqUser": _billReqUser,
            "payerPhone": _payerPhone,
            "payerEmail": _payerEmail,
            "paymentOption": _paymentOption,
            "billReference": _billReference,
            "revenueSourceId": _revenueSourceId,
            "zoneId": _zoneId,
            "indexNo": _indexNo,
            "is25Percent": _is25Percent
        })
        headers = {
        'Content-Type': 'application/json'
        }
        response ={}
        try:

            response = requests.request(Api.Methods.POST, url, headers=headers, data=payload)
            
            return  response
          
        except:
           
            return  response

    @staticmethod
    def check_control_number_status(billId):
        url =  Api.URLS.CHECK_CONTROL_NUMBER_STATUS_BASE_URL+f"Id={billId}"
        response = requests.request(Api.Methods.GET, url,)
        if response.status_code == 200:
            return  json.loads(response.text)
        return json.loads(response.text)





    
