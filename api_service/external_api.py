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
        url = Api.NECTA_APPLICANT_INFORMATION_BASE_URL
    
        payload = CallExternalApi.getparems(
            index_no=index_no,exam_year=exam_year,
            exam_id=exam_id, api_key=api_key)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request(Api.POST, url, headers=headers, data=payload)

        json_data = json.loads(response)
    
        return json_data

    @staticmethod
    def applicant_loan_Status(index_no):
        url = f"{Api.BENFICIARY_OR_25_PERCENT_BASE_URL}?indexNo={index_no}"
        response = requests.request(Api.GET, url)
        return response

        
        

    
