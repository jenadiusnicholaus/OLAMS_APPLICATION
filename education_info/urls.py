
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('check-school-existance/', CheckSchoolExistence.as_view()),
    path('education-informations/', ApplicantEducationInformation.as_view()),
    path('education-information/confirm/', EducationConfirmation.as_view()),
]