


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . views import *
router = routers.DefaultRouter()
# router.register(r'search-applicant',SearchNetaApplicantViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('applicant-category/', ApplicantCategoryViewSet.as_view()),
    path('search-applicant/', SearchNetaApplicantViewSet.as_view()),

]
