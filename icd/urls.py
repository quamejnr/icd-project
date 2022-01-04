from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view (
    openapi.Info(
        title='ICD10 Codes API',
        default_version='icd10',
        description='API for ICD10 Codes',
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name='BSD License')
    )
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('icd10/', include('icd10.urls')),
    path('account/', include('dj_rest_auth.urls')),
    path('account/registration', include('dj_rest_auth.registration.urls')),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
