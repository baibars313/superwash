from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/main_services', Main_services_viewset, basename='user')

urlpatterns = [
    path('api/',Main_services_viewset.as_view({'get': 'list'}), name='main_services'),
    path('addNft/',AddNft.as_view()),
    path('change/<int:pk>/',ChangeStatus.as_view()),
    path('checkuser/<int:pk>/',Checkuser.as_view())
]+router.urls