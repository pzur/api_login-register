from rest_framework import serializers, viewsets
from .models import Cliente, Mascota, Paseador

class PaseadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paseador 
        fields = ['idpas','nombre','apellido','direccion','rating','titulo','descripcion','foto']

class MascotaSerializer(serializers.ModelSerializer):
    pash =PaseadorSerializer(many=True, read_only=True)
    class Meta:
        model = Mascota
        fields = ['idmas','nombre','raza','edad','peso','sexo','tipo_mascota','foto','descripcion','pash']

class ClientesSerializer(serializers.ModelSerializer):
    dueño=MascotaSerializer(many=True)
    class Meta:
        model = Cliente
        fields = ['idcli','nombre','apellido','direccion','telefono','correo','foto','dueño']
