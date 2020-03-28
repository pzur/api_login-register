from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Cliente, Mascota, Paseador
from rest_framework import viewsets,permissions,authentication
from .serializer import ClientesSerializer,MascotaSerializer, PaseadorSerializer

class ClienteList(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class MascotaList(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class PaseadorList(viewsets.ModelViewSet):
    queryset = Paseador.objects.all()
    serializer_class = PaseadorSerializer

from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
import json

class Registros(generics.CreateAPIView):
    permissions_classes = [permissions.AllowAny]
    def post(self,request,*args, **kwargs):
        #Creando un nuevo Usuario
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user= User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        #generando el token para el usuario
        token=Token.objects.create(user=user)
        data={'detail':'Usuario creado ok con token:'+token.key}
        dump = json.dumps(data)
        return HttpResponse(dump,content_type='application/json')

from rest_framework.views import APIView
from django.contrib.auth import authenticate
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            data = {"token": 'ola gente: ' +user.auth_token.key} 
        else:
            data = {"error": "No Son las Credenciales XD"}
        respuesta = json.dumps(data)
        return HttpResponse(respuesta,content_type='application/json')
