
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

urlpatterns = [
    path('profile/',  ApplicatProfileInfo.as_view() )

]