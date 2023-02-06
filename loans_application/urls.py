


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('applicant-type/', ApplicantTypeViewSet.as_view()),
    path('search-applicant/', SearchNectaApplicantViewSet.as_view()),
    path('add-applicant-attented-school/', AddSchoolView.as_view()),
    path('applicant-existance/', ApplicantExistenceView.as_view()),
    path('pre-applicant-necta-contact-infos/', PreAplicantNectAContactInfosView.as_view()),
    path('pre-applicant-none-necta-contact-infos/', PreAplicantNoneNectAContactInfosView.as_view()),
    path('choose-apploicant-category/', ChooseApplicantCategory.as_view())
]
