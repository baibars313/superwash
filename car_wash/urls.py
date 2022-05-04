from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/main_services', Main_services_viewset, basename='user')

urlpatterns = [
    path('api/',Main_services_viewset.as_view({'get': 'list'}), name='main_services'),
    path('addNft/',AddNft.as_view()),
    path('sale/<int:pk>/',Createsale.as_view()),
    path('checkuser/<str:pk>/',Checkuser.as_view()),
    path('onsale/',Onsale.as_view()),
    path('owned/',owned.as_view()),
    path('adduser/',Adduser.as_view()),
]+router.urls