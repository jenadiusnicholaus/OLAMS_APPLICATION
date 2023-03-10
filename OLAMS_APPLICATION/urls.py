
from django.contrib import admin
from django.urls import path, include

# from django.contrib.auth.models import User
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


# Routers provide a way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/application/', include('loans_application.urls')),
    path('api/education-info/', include('education_info.urls')),
    path('api/demographics/', include('demographics.urls')),
    path('api/applicant-profile/', include('applicantProfile.urls')),
    path('api/preliminary/',include('preliminary_info.urls')),
    path('api/guarantors/',include('guarantordetails.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
