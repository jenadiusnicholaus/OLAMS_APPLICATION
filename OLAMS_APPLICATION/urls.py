
from django.contrib import admin
from django.urls import path, include

# from django.contrib.auth.models import User
from django.urls import include, path


# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/application/', include('loans_application.urls')),
    path('api/education-info/', include('education_info.urls')),
    path('api/demographics/', include('demographics.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

