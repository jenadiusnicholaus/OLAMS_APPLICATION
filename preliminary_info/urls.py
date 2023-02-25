from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'preliminary-info3', PreliminaryInfoView,basename='preliminary-info3')


urlpatterns = [
    path('preliminary-info/', include(router.urls)),
]