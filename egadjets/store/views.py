from django.shortcuts import render
from .serializers import productModelSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import product
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action



# Create your views here.


class productView(APIView):
    def get(self,request):
        prod=product.objects.all()
        dser=productModelSerializer(prod,many=True)
        return Response(data=dser.data)
    def post(self,request):
        ser=productModelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"ok"})
        return Response(data=ser.errors)

class SpecificProductView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id") 
        prod=product.objects.get(id=id)
        dser=productModelSerializer(prod)
        return Response(data=dser.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        prod=product.objects.get(id=id)
        prod.delete()
        return Response({"msg":"deleted"})
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        prod=product.objects.get(id=id)
        ser=productModelSerializer(data=request.data,instance=prod)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        return Response(data=ser.errors)
    

class productVset(ViewSet):
    def retrieve(self,request,*args,**kwargs):
        pid=kwargs.get("pk")
        prod=product.objects.get(id=pid)
        dser=productModelSerializer(prod)
        return Response(data=dser.data)
    def list(self,request):
        prodlist=product.objects.all()
        dser=productModelSerializer(prodlist,many=True)
        return Response(data=dser.data)
    def create(self,request):
        ser=productModelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def update(self,request,*args,**kwargs):
        pid=kwargs.get("pk")
        prod=product.objects.get(id=pid)
        ser=productModelSerializer(data=request.data,instance=prod)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def destroy(self,request,*args,**kwargs):
        pid=kwargs.get("pk")
        prod=product.objects.get(id=pid)
        prod.delete()
        return Response({"msg":"DELETED"}) 
    @action(methods=["GET"],detail=False)
    def category(self,request,*args,**kwargs):
        cat=product.objects.values_list("category",flat=True).distinct()
        return Response(data=cat)
    

from rest_framework.viewsets import ModelViewSet  
from .serializers import UserSerializer
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class productMVSet(ModelViewSet):
    serializer_class=productModelSerializer
    queryset=product.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]



# django rest authentication
class UserVSet(ViewSet):
    def create(self,request):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"})
        return Response({"msg":"failed"})