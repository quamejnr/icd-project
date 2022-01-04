from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from icd10.views import FileUploadView, CategoryViewset, ICDViewset
from django.urls import path, include

router = DefaultRouter()

router.register('categories', CategoryViewset, basename='category')
router.register('codes', ICDViewset, basename='code')


urlpatterns = [
    path('', include(router.urls)),
    path('upload-file/', FileUploadView.as_view(), name='upload-file')
]