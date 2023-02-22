
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('check-school-existance/', CheckSchoolExistence.as_view()),
    path('education-informations/', ApplicantEducationInformationView.as_view()),
    path('education-formfour-seatings/', FormFourDetailsView.as_view()),
    path('rducation-formSix-details/', FormSixDetailsView.as_view()),
    path('education-diplomaDetails/',DiplomaDetailsView.as_view()),
    path('education-tertiaryEducation/',TertiaryEducationView.as_view()),
    path('education-bachelorAwards/',TertiaryEducationBachelorAwardsView.as_view()),
    path('education-masterAwards/',MasterDegreeAwardView.as_view()),
    path('education-information/confirm/', EducationConfirmation.as_view()),
    path('education-tertiaryInfo/confirm/',TertiaryEducationConfirmation.as_view())
]