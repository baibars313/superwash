from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import main_services
from .serializers import model_serializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.http import JsonResponse

class Main_services_viewset(ReadOnlyModelViewSet):
    queryset = main_services.objects.all()
    serializer_class = model_serializer

# @api_view(['GET'])
# def home_page(request):
#     if request.method == 'GET':
#         main_service=main_services.objects.all()
#         serialized=model_serializer(main_service)
#         print(serialized.data)
#         return Response(serialized.data)








