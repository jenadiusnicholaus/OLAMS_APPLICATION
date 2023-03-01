
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'regiion', DemographicRegionViewSet)
router.register(r'district',  DemographicDistrictViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('applicantDemographicsDetails/',
         ApplicantDemographicsDetails.as_view()),
    path('confirm-demographics-infos/', ConfirmDemographicsView.as_view())
]
