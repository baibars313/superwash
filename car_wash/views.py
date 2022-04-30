from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AllNfts
from .serializers import model_serializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.http import JsonResponse

# Create your views here.
class Main_services_viewset(ReadOnlyModelViewSet):
    queryset = AllNfts.objects.all()
    serializer_class = model_serializer