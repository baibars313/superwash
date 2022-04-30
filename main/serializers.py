from rest_framework import serializers
from .models import *

class model_serializer(serializers.ModelSerializer):
    class Meta:
        model= main_services
        fields = '__all__'