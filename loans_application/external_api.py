import requests
import json
from utils.constants import Constants

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
        url = Constants.url
    
        payload = CallExternalApi.getparems(
            index_no=index_no,exam_year=exam_year,
            exam_id=exam_id, api_key=api_key)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        json_data = json.loads(response.text)
        return json_data
        
        

    
