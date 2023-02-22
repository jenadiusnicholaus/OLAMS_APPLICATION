from django.shortcuts import render
from education_info.models import *
from rest_framework.response import Response
from rest_framework import generics, decorators, permissions, status
from . serializers import *
from rest_framework.views import APIView



class CheckSchoolExistence(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        if request.data:
            _center_number = request.data['center_number']
            try:
                schoool = TBL_Education_ApplicantAttendedSchool.objects.get(center_number = _center_number)
                school_serializer = ApplicantSchoolInformationSerializer(instance=schoool)
                response_obj = {
                        "success": False,
                        'status_code': status.HTTP_200_OK,
                        "message": "Found",
                        "data": school_serializer.data
                        
                        }
                return Response(response_obj)
            except:
                response_obj = {
                        "success": False,
                        'status_code': status.HTTP_404_NOT_FOUND,
                        "message": "No found",
                        
                        }
                return Response(response_obj)
        response_obj = {
                        "success": False,
                        'status_code': status.HTTP_400_BAD_REQUEST,
                        "message": "No params sepecified",
                        
                        }
        return Response(response_obj)
class ApplicantEducationInformationView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        _profileId = request.data['profileId']
        _f4_no_of_seat =request.data['noOfSeat']
        _pst4ed =request.data['postFormFour']
        _f4sps = request.data['formFourSponsorship']
        _f4sps_cp = request.data['formFourSponsorContactPerson']
        _f4sps_cp_phone = request.data['formFourSponsorPhoneNo']
        _f4sps_cp_addr = request.data['formFourSponsorAddress']
        _pst4sps =request.data['postFormFourSponsorship']
        _pst4sps_cp = request.data['postFormFourContactPerson']
        _pst4sps_cp_phone = request.data['postFormFourSponsorPhoneNo']
        _pst4sps_cp_addr = request.data['postFormFourSponsorAddress']
        _ay = request.data['applicationYear']
        _confirm = False
        applicantprofile = TblAppProfile.objects.get(id=_profileId)
        educationInfo = TBL_EducationInfo.objects.filter(applicant=applicantprofile,ay=_ay)
        if educationInfo.exists():
            response_obj = {
                "success": False,
                'status_code': status.HTTP_200_OK,
                "message": "Education Information Exists",
            }
            return Response(response_obj)
        else:
            created = TBL_EducationInfo.objects.create(
                applicant =applicantprofile,
                f4_no_of_seat = _f4_no_of_seat,
                pst4ed = _pst4ed,
                f4sps = _f4sps,
                f4sps_cp=_f4sps_cp,
                f4sps_cp_phone=_f4sps_cp_phone,
                f4sps_cp_addr=_f4sps_cp_addr,
                pst4sps=_pst4sps,
                pst4sps_cp=_pst4sps_cp,
                pst4sps_cp_phone=_pst4sps_cp_phone,
                pst4sps_cp_addr=_pst4sps_cp_addr,
                ay=_ay,
                confirm=_confirm,
            )
            if created:
                response_obj = {
                    "success": True,
                    'status_code': status.HTTP_200_OK,
                    "message": "Education Information Saved",
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    'status_code': status.HTTP_200_OK,
                    "message": "There is an error please try again",
                }
                return Response(response_obj)
    def get(self,request, *args,**kwargs):
        _profileId = request.data['profileId']
        _ay = request.data['applicationYear']
        #applicantprofile = TBL_App_Profile.objects.get(id=_profileId)
        educationInformation = TBL_EducationInfo.objects.get(applicant=_profileId, ay=_ay)
        educationInfoserializer = EducationInfoSerializer(instance=educationInformation)
        if educationInfoserializer is None:
            response_obj = {
                "success": False,
                'status_code': status.HTTP_204_NO_CONTENT,
                "message": "You did not fill any education information for thia application year",
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": True,
                'status_code': status.HTTP_200_OK,
                "message": "Demographics Info Found",
                "data": educationInfoserializer.data
            }
            return Response(response_obj)

    def put(self, request,*args, **kwargs):
        _ay = request.data['applicationYear']
        _profileId = request.data['profileId']
        _f4_no_of_seat = request.data['noOfSeat']
        _pst4ed = request.data['postFormFour']
        _f4sps = request.data['formFourSponsorship']
        _f4sps_cp = request.data['formFourSponsorContactPerson']
        _f4sps_cp_phone = request.data['formFourSponsorPhoneNo']
        _f4sps_cp_addr = request.data['formFourSponsorAddress']
        _pst4sps = request.data['postFormFourSponsorship']
        _pst4sps_cp = request.data['postFormFourContactPerson']
        _pst4sps_cp_phone = request.data['postFormFourSponsorPhoneNo']
        _pst4sps_cp_addr = request.data['postFormFourSponsorAddress']
        _confirm =0
        #applicantprofile = TblAppProfile.objects.get(id=_applicant)
        informationForEdit = TBL_EducationInfo.objects.filter(applicant=_profileId,ay=_ay,confirm=_confirm).first()
        if informationForEdit is not None:
            dataToEdit = {
                'confirm': _confirm,
                'f4_no_of_seat': _f4_no_of_seat,
                'pst4ed': _pst4ed,
                'f4sps': _f4sps,
                'f4sps_cp': _f4sps_cp,
                'f4sps_cp_phone': _f4sps_cp_phone,
                'f4sps_cp_addr': _f4sps_cp_addr,
                'pst4sps': _pst4sps,
                'pst4sps_cp': _pst4sps_cp,
                'pst4sps_cp_phone': _pst4sps_cp_phone,
                'pst4sps_cp_addr': _pst4sps_cp_addr
            }
            educationInforSerializer = EducationInfoSerializer(informationForEdit, data=dataToEdit, partial=True)
            if educationInforSerializer.is_valid():
                educationInforSerializer.save()
                response_obj ={
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Education info Not Found"
            }
            return Response(response_obj)
class FormFourDetailsView(APIView): #Other form four seating's Details
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        _second_seat_index_no = request.data['otherFormFourIndexno']
        _third_seat_index_no = request.data['otherFormFourIndexno2']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        formFourDetails = TBL_Education_FormFourInfos.objects.filter(app_year=_app_year, applicant=_applicant).first()
        if formFourDetails.exist():
            response_obj ={
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "Form four Details Updated successfully"
            }
            return  Response(response_obj)
        else:
            created = TBL_Education_FormFourInfos.objects.create(
                applicant=applicantprofile,
                app_year=_app_year,
                second_seat_index_no=_second_seat_index_no,
                third_seat_index_no=_third_seat_index_no,
            )
            if created:
                response_obj ={
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Other form four seats saved Successfully"
                }
                return Response(response_obj)
    def get(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        formFourDetails = TBL_Education_FormFourInfos.objects.get(app_year=_app_year, applicant=_applicant)
        formFourSerializer = FormfourInformationSerializer(instance=formFourDetails)
        if formFourSerializer is not None:
            response_obj ={
                "success": True,
                "status": status.HTTP_200_OK,
                "data": formFourDetails.data,
            }
            return  response_obj
        else:
            response_obj ={
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no other form four seating"
            }
            return Response(response_obj)
    def put(self, request, *args,**kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        _second_seat_index_no = request.data['otherFormFourIndexno']
        _third_seat_index_no = request.data['otherFormFourIndexno2']
        informationForEdit = TBL_Education_FormFourInfos.objects.filter(applicant = _applicant, app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                'second_seat_index_no': _second_seat_index_no,
                'third_seat_index_no': _third_seat_index_no,
            }
            form4detailserializer = FormfourInformationSerializer(informationForEdit, data=dataToEdit, partial=True)
            if form4detailserializer.is_valid():
                form4detailserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Education info Not Found"
            }
            return Response(response_obj)
class FormSixDetailsView(APIView): ######### FORM SIX DETAILS #####################
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        _f6index_no = request.data['f6Indexno']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        formSixDetails = TBL_Education_FormSixInfos.objects.filter(app_year=_app_year, applicant=_applicant).first()
        if formSixDetails.exist():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "Form six Details Updated successfully"
            }
            return Response(response_obj)
        else:
            created = TBL_Education_FormSixInfos.objects.create(
                applicant=applicantprofile,
                app_year=_app_year,
                f6index_no=_f6index_no,
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form six details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        formsixdetails = TBL_Education_FormSixInfos.objects.get(app_year=_app_year, applicant=_applicant)
        formsixserializer = FormsixInformationSerializer(instance=formsixdetails)
        if formsixserializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": formsixserializer.data,
            }
            return response_obj
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no form six details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        _f6index_no = request.data['f6Indexno']
        informationForEdit = TBL_Education_FormSixInfos.objects.filter(applicant=_applicant,
                                                     app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                'f6index_no': _f6index_no,
            }
            form6detailserializer = FormsixInformationSerializer(informationForEdit, data=dataToEdit, partial=True)
            if form6detailserializer.is_valid():
                form6detailserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form six information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form six info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Form six info Not Found"
            }
            return Response(response_obj)
class DiplomaDetailsView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _applicant = request.data['profileId']
        _diplomaInstitution= request.data['diplomaInstitution']
        _avn = request.data['avn']
        _entryYear = request.data['entryYear']
        _graduateYear = request.data['graduatedYear']
        _gpa = request.data['gpa']
        _registrationNumber = request.data['registrationNo']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        diplomadetails = TblDiplomaDetails.objects.filter(app_year=_app_year, applicant=_applicant).first()
        if diplomadetails.exist():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "Diploma Details already exist for this year"
            }
            return Response(response_obj)
        else:
            created = TblDiplomaDetails.objects.create(
                applicant=applicantprofile,
                app_year=_app_year,
                diplomaInstitution=_diplomaInstitution,
                avn = _avn,
                entryYear = _entryYear,
                graduateYear = _graduateYear,
                gpa = _gpa,
                registrationNumber=_registrationNumber
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form Diploma details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _app_year = request.data['applicationYear']
        diplodetails = TblDiplomaDetails.objects.get(app_year=_app_year, applicant=_applicant)
        diplodetailserializer = DiplomaInformationSerializer(instance=diplodetails)
        if diplodetailserializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": diplodetailserializer.data,
            }
            return response_obj
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no diploma details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _applicant = request.data['profileId']
        _diplomaInstitution = request.data['diplomaInstitution']
        _avn = request.data['avn']
        _entryYear = request.data['entryYear']
        _graduateYear = request.data['graduatedYear']
        _gpa = request.data['gpa']
        _registrationNumber = request.data['registrationNo']
        informationForEdit = TblDiplomaDetails.objects.filter(applicant=_applicant,
                                                                       app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                'diplomaInstitution': _diplomaInstitution,
                'avn':_avn,
                'entryYear': _entryYear,
                'graduateYear': _graduateYear,
                'gpa': _gpa,
                'registrationNumber':_registrationNumber,
            }
            form6detailserializer = FormsixInformationSerializer(informationForEdit, data=dataToEdit, partial=True)
            if form6detailserializer.is_valid():
                form6detailserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Diploma information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Form Diploma info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Diploma info Not Found"
            }
            return Response(response_obj)

class TertiaryEducationView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request, *args,**kwargs):
        _applicationYear = request.data['applicationYear']
        _applicant = request.data['profileId']
        _admittedInstitute= request.data['admittedInst']
        _admittedCourse = request.data['admittedCourse']
        _admittedDegreeCategory =request.data['admittedDegree']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        institutionadmitted = Institutions.objects.get(id=_admittedInstitute)
        courseadmitted =TblCourses.objects.get(id =_admittedCourse)
        tertiaryinfo = TBL_Education_TertiaryEducationInfos.objects.filter(applicant=_applicant,
                                                                       applicationYear=_applicationYear)
        if tertiaryinfo.exist():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "Tertiary Education Details already exist for this year"
            }
            return Response(response_obj)
        else:
            created = TblDiplomaDetails.objects.create(
                applicationYear=_applicationYear,
                applicant = applicantprofile,
                admittedInstitute = institutionadmitted,
                admittedCourse = courseadmitted,
                admittedDegreeCategory =_admittedDegreeCategory,
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Tertiary details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _applicationYear = request.data['applicationYear']
        _applicant = request.data['profileId']
        tertiaryInfo = TBL_Education_TertiaryEducationInfos.objects.get(applicationYear=_applicationYear, applicant=_applicant)
        tertiaryInfoSerializer = TertiaryEducationSerializer(instance=tertiaryInfo)
        if tertiaryInfoSerializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": tertiaryInfoSerializer.data,
            }
            return response_obj
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no Tertiary education details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _applicationYear = request.data['applicationYear']
        _applicant = request.data['profileId']
        _admittedInstitute = request.data['admittedInst']
        _admittedCourse = request.data['admittedCourse']
        _admittedDegreeCategory = request.data['admittedDegree']
        institutionadmitted = Institutions.objects.get(id=_admittedInstitute)
        courseadmitted = TblCourses.objects.get(id=_admittedCourse)
        informationForEdit = TBL_Education_TertiaryEducationInfos.objects.filter(applicant=_applicant,
                                                              applicationYear=_applicationYear).first()
        if informationForEdit is not None:
            dataToEdit = {
                'admittedInstitute': institutionadmitted,
                'admittedCourse': courseadmitted,
                'admittedDegreeCategory': _admittedDegreeCategory,
            }
            tertiaryInforSerializer = TertiaryEducationSerializer(informationForEdit, data=dataToEdit, partial=True)
            if tertiaryInforSerializer.is_valid():
                tertiaryInforSerializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Tertiary information Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Tertiary info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Tertiary info Not Found"
            }
            return Response(response_obj)
class TertiaryEducationBachelorAwardsView(APIView): #############  BACHELOR DEGREE AWARD DETAILS FOR PGD ##############
    authentication_classes = []
    permission_classes = []
    def post(self,request,*args,**kwargs):
        _applicant= request.data['profileId']
        _award= request.data['award']
        _regno = request.data['regno']
        _entryYear = request.data['entryYear']
        _graduateYear = request.data['graduateYear']
        _gpa = request.data['gpa']
        _app_year = request.data['applicationYear']
        _institution = request.data['institutionGraduated']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        awardedinstitution = Institutions.objects.get(id=_institution)
        bachelorAward = TblTertiaryEducationBachelorAwards.objects.filter(applicant=_applicant,
                                                                           applicationYear=_institution)
        if bachelorAward.exist():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "This Award already exist for this year"
            }
            return Response(response_obj)
        else:
            created = TblTertiaryEducationBachelorAwards.objects.create(
                applicant=applicantprofile,
                award = _award,
                regno = _regno,
                entryYear = _entryYear,
                graduateYear = _graduateYear,
                gpa = _gpa,
                app_year =_app_year,
                institution = awardedinstitution
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Tertiary details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _applicant = request.data['profileId']
        bachelorAwards = TblTertiaryEducationBachelorAwards.objects.get(applicationYear=_app_year,
                                                                        applicant=_applicant)
        bachelorawardserializer = BachelorDegreeAwardSerializer(instance=bachelorAwards)
        if bachelorawardserializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": bachelorawardserializer.data,
            }
            return response_obj
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no Bachelor degree details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _award = request.data['award']
        _regno = request.data['regno']
        _entryYear = request.data['entryYear']
        _graduateYear = request.data['graduateYear']
        _gpa = request.data['gpa']
        _app_year = request.data['applicationYear']
        _institution = request.data['institutionGraduated']
        awardedinstitution = Institutions.objects.get(id=_institution)
        informationForEdit = TblTertiaryEducationBachelorAwards.objects.filter(applicant=_applicant,
                                                                                 app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                "award": _award,
                "regno": _regno,
                "entryYear": _entryYear,
                "graduateYear": _graduateYear,
                "gpa": _gpa,
                "institution": awardedinstitution
            }
            bachelorawardserializer = BachelorDegreeAwardSerializer(informationForEdit, data=dataToEdit, partial=True)
            if bachelorawardserializer.is_valid():
                bachelorawardserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Bachelor degree award Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Bachelor degree info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Bachelor degree info Not Found"
            }
            return Response(response_obj)
class MasterDegreeAwardView(APIView):  ###### MASTER DEGREE AWARD DETAILS FOR PGD  ###########
    authentication_classes = []
    permission_classes = []
    def post(self,request,*args,**kwargs):
        _applicant= request.data['profileId']
        _master_award= request.data['masterAward']
        _regNo = request.data['masterRegNo']
        _entryYear = request.data['masterEntryYear']
        _graduateYear = request.data['masterGraduateYear']
        _gpa = request.data['masterGpa']
        _app_year = request.data['applicationYear']
        _institution = request.data['institutionGraduated']
        applicantprofile = TblAppProfile.objects.get(id=_applicant)
        awardedinstitution = Institutions.objects.get(id=_institution)
        masterAward = TblTertiaryEducationMasterAward.objects.filter(applicant=_applicant,
                                                                           applicationYear=_institution)
        if masterAward.exist():
            response_obj = {
                "success": False,
                "status_code": status.HTTP_200_OK,
                "message": "This Award already exist for this year"
            }
            return Response(response_obj)
        else:
            created = TblTertiaryEducationMasterAward.objects.create(
                applicant=applicantprofile,
                master_award = _master_award,
                regNo = _regNo,
                entryYear = _entryYear,
                graduateYear = _graduateYear,
                gpa = _gpa,
                app_year =_app_year,
                institution = awardedinstitution
            )
            if created:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Master details saved Successfully"
                }
                return Response(response_obj)

    def get(self, request, *args, **kwargs):
        _app_year = request.data['applicationYear']
        _applicant = request.data['profileId']
        masterAwards = TblTertiaryEducationMasterAward.objects.get(applicationYear=_app_year,
                                                                        applicant=_applicant)
        masterrawardserializer = MasterDegreeAwardSerializer(instance=masterAwards)
        if masterrawardserializer is not None:
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "data": masterrawardserializer.data,
            }
            return response_obj
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "You have no Master degree details for this year"
            }
            return Response(response_obj)

    def put(self, request, *args, **kwargs):
        _applicant = request.data['profileId']
        _master_award = request.data['masterAward']
        _regNo = request.data['masterRegNo']
        _entryYear = request.data['masterEntryYear']
        _graduateYear = request.data['masterGraduateYear']
        _gpa = request.data['masterGpa']
        _app_year = request.data['applicationYear']
        _institution = request.data['institutionGraduated']
        awardedinstitution = Institutions.objects.get(id=_institution)
        informationForEdit = TblTertiaryEducationMasterAward.objects.filter(applicant=_applicant,
                                                                                 app_year=_app_year).first()
        if informationForEdit is not None:
            dataToEdit = {
                "master_award": _master_award,
                "regNo": _regNo,
                "entryYear": _entryYear,
                "graduateYear": _graduateYear,
                "gpa": _gpa,
                "institution": awardedinstitution
            }
            masterawardserializer = MasterDegreeAwardSerializer(informationForEdit, data=dataToEdit, partial=True)
            if masterawardserializer.is_valid():
                masterawardserializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Master degree award Updated Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Master degree info Failed to Updated"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "Master degree info Not Found"
            }
            return Response(response_obj)
class EducationConfirmation(APIView): ########### CONFIRM EDUCATION INFORMATION ################
    authentication_classes = []
    permission_classes = []
    def put(self, request, *args,**kwargs):
        _applicant = request.data['profileId']
        _ay = request.data['applicationYear']
        _confirm = 0
        _confirmed =1
        dataToConfirm = TBL_EducationInfo.objects.filter(applicant=_applicant,ay=_ay,confirm=_confirm).first()
        if dataToConfirm is not None:
            confirmSerializer = ConfirmEducationInfoSerializer(dataToConfirm, data={'confirm': _confirmed}, partial=True)
            if confirmSerializer.is_valid():
                confirmSerializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Education information Confirmed Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "There is an error on Confirm Education Information"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "No matching education information found"
            }
            return Response(response_obj)
class TertiaryEducationConfirmation(APIView):
    authentication_classes = []
    permission_classes = []
    def put(self, request, *args,**kwargs):
        _applicant = request.data['profileId']
        _applicationYear = request.data['applicationYear']
        _confirm = 0
        _confirmed =1
        dataToConfirm = TBL_Education_TertiaryEducationInfos.objects.filter(applicant=_applicant,applicationYear=_applicationYear,confirm=_confirm).first()
        if dataToConfirm is not None:
            confirmSerializer = ConfirmTertiaryEducationSerializer(dataToConfirm, data={'confirm': _confirmed}, partial=True)
            if confirmSerializer.is_valid():
                confirmSerializer.save()
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": " Tertiary Education information Confirmed Successfully"
                }
                return Response(response_obj)
            else:
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "There is an error on Confirm Tertiary Education Information"
                }
                return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "No matching Tertiary education information found"
            }
            return Response(response_obj)