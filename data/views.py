from django.shortcuts import render
from data.models import Data,Customer
from data.serializers import DataSerializers, CustomerSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DataList(APIView):
    def get(self,request,format=None):
        data = Data.objects.all()
        serializers = DataSerializers(data,many=True)
        return Response(serializers.data)
    
    def post(self, request,format=None):
        serializers = DataSerializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class DataDetail(APIView):
    def get(self,request,pk,format=None):
        data = Data.objects.get(pk=pk)
        serializers = DataSerializers(data)
        return Response(serializers.data)
    
    def put(self,request,pk,format=None):
        value = Data.objects.get(pk=pk)
        serializers = DataSerializers(value, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        val = Data.objects.get(pk=pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerList(APIView):
    def get(self,request,format=None):
        val = Customer.objects.all()
        serializers = CustomerSerializers(val,many=True)
        return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = CustomerSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    def get(self,request,pk,format=None):
        val = Customer.objects.get(pk=pk)
        serializers = CustomerSerializers(val)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        val = Customer.objects.get(pk=pk)
        serializers = CustomerSerializers(val,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)