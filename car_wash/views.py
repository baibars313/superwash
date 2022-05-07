from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AllNfts
from .serializers import *
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# all item returned
class Main_services_viewset(ReadOnlyModelViewSet):
    queryset = AllNfts.objects.all()
    serializer_class = model_serializer




# addding new nft
class AddNft(APIView):
    def post(self, request, format=None):
        serializer = model_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# checking use new or not
class Createsale(APIView):
    def get_object(self, pk):
        try:
            return AllNfts.objects.get(itemid=pk)
        except AllNfts.DoesNotExist:
            raise Http404

   
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = model_serializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"success"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# check user new or not
class Checkuser(APIView):
    def get_object(self,pk):
        try:
            return Nftuser.objects.get(address=pk)
        except Nftuser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = User_serializer(snippet)
        return Response({"msg":"success","data":[serializer.data]})



# returning all on sale items of user
class Onsale(generics.ListAPIView):
    serializer_class = model_serializer

    def get_queryset(self):
        user = self.request.query_params.get('address')
        return AllNfts.objects.filter(seller=user)
        # print(self.request.query_params.get('address'))

# returning all owned nfts
class owned(generics.ListAPIView):
    serializer_class = model_serializer

    def get_queryset(self):
        user = self.request.query_params.get('address')
        return AllNfts.objects.filter(owner=user)
        # print(self.request.query_params.get('address'))
        
# adding new user
class Adduser(APIView):
    def post(self, request, format=None):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        

