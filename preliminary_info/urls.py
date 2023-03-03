from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'preliminary-info-save', PreliminaryInfoView,basename='preliminary-info-save')
router.register(r'preliminary-parent-info', ParentInfoView,basename='preliminary-parent-info')
router.register(r'preliminary-parent-death',ParentDeathInfoView,basename='preliminary-parent-death')

urlpatterns = [
    path('preliminary-info/', include(router.urls)),
]