
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'LugGurantorDetails',GuarantorDetailsLUGViewSet, basename='LugGurantorDetails')
router.register(r'PgdGurantorDetails',GuarantorDetailsPGDViewSet, basename='PgdGurantorDetails')
urlpatterns = [
    path('', include(router.urls)),
    path('guarantorDetails/', include(router.urls)),
]