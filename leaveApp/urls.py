
from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import url
from django.urls import include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Leave App API",
        default_version='v1',
        description="Leave app API",
        terms_of_service="",
        contact=openapi.Contact(email="anmolk3797@gmail.com"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    path("admin/", admin.site.urls),
    path("account/",include('account.urls')),
    path("leave/",include('leaveRequest.urls')),

]
