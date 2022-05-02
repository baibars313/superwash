from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AllNfts
from .serializers import model_serializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class Main_services_viewset(ReadOnlyModelViewSet):
    queryset = AllNfts.objects.all()
    serializer_class = model_serializer





class AddNft(APIView):
    def post(self, request, format=None):
        serializer = model_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangeStatus(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
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

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class Checkuser(APIView):

    def get_object(self, pk):
        try:
            return AllNfts.objects.filter(status=pk)
        except AllNfts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = model_serializer(snippet)
        return Response({"msg":"success","data":serializer.data})

