from usercategory.models import *
from applicantProfile.models import  TBL_App_Profile
from loans_application .necta_serializers import UserProfileSerialiozer
from rest_framework.response import Response
from rest_framework import  status



class RandUtils:

    @staticmethod
    def upadate_or_create_user_category(user, benef_categiory):
        UserCategory.objects.get_or_create(
            user = user,
            beneficiary = benef_categiory,
        )

    @staticmethod
    def getApplicantProfile(_index_no,  _app_year):
        if _index_no.startswith('S') or _index_no.startswith('P'):
              
                get_applicant_profile_app_year = TBL_App_Profile.objects.filter(
                    applicant__applicant_details__applicant_type__necta__index_no__exact = _index_no,
                     applicant__app_year = _app_year
                      ). first()
                

                profileSerializer = UserProfileSerialiozer(
                    instance =  get_applicant_profile_app_year
                    )
               
                response_obj = {
                            "success": False,
                            'status_code': status.HTTP_200_OK,
                            "message": "Process Necta",\
                            'data': profileSerializer.data
                        
                            
                            }
                return Response(response_obj)
                    
                
        elif _index_no.startswith('E'):
                get_applicant_profile_app_year = TBL_App_Profile.objects.filter(
                    applicant__applicant_details__applicant_type__none_necta__index_no__exact = _index_no,
                     applicant__app_year = _app_year
                      ). first()
                

                profileSerializer = UserProfileSerialiozer(
                    instance =  get_applicant_profile_app_year
                    )
               
                response_obj = {
                            "success": False,
                            'status_code': status.HTTP_200_OK,
                            "message": "Process Necta",
                            'data': profileSerializer.data
                        
                            
                            }
                return Response(response_obj)