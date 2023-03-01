
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'post-form-four', PostFormFourTypeViewSet)
router.register(r'applicant-sponsors', ApplicantSponsorshipViewSet)
router.register(r'institutes', DiplomaInstitutesViewSet)
router.register(r'tertiary_institute', TertiaryInstitutesViewSet)
router.register(r'courses', CoursesViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('check-school-existance/', CheckSchoolExistence.as_view()),
    path('education-informations/', ApplicantEducationInformationView.as_view()),
    path('education-formfour-seatings/', FormFourDetailsView.as_view()),
    path('education-formSix-details/', FormSixDetailsView.as_view()),
    path('education-diplomaDetails/', DiplomaDetailsView.as_view()),
    path('education-tertiaryEducation/', TertiaryEducationView.as_view()),
    path('education-bachelorAwards/',
         TertiaryEducationBachelorAwardsView.as_view()),
    path('education-masterAwards/', MasterDegreeAwardView.as_view()),
    path('education-information/confirm/', EducationConfirmation.as_view()),
    path('education-tertiaryInfo/confirm/',
         TertiaryEducationConfirmation.as_view())
]
