from rest_framework import serializers
from .models import *

class model_serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','uri','price','status','itemid','datetime','owner','seller')
        model= AllNfts

class User_serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=Nftuser