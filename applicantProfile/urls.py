
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'upload-photo', UploadApplicantPhotoView)


urlpatterns = [
    path('applicant/', include(router.urls)),
    path('profile/', ApplicatProfileInfoView.as_view())

]
