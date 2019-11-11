from ..models import Proyecto , Cliente , Tecnologia , Colaborador
from . import serializers
from rest_framework import generics , status
from rest_framework.response import Response


class ProyectoListView(generics.ListAPIView) :
    serializer_class =  serializers.ProyectoSerializer

    def get_queryset(self):
        return Proyecto.objects.filter(activo = True)

class ProyectoDetailView(generics.RetrieveAPIView) :
    queryset = Proyecto.objects.all()
    serializer_class =  serializers.ProyectoDetailSerializer

class ClienteListView(generics.ListAPIView) :
    queryset = Cliente.objects.all()
    serializer_class =  serializers.ClienteSerializer

class TecnologiasListView(generics.ListAPIView) : 
    queryset = Tecnologia.objects.all()
    serializer_class =  serializers.TecnologiaSerializer

class ColaboradorListView(generics.ListAPIView) : 
    queryset = Colaborador.objects.all()
    serializer_class =  serializers.ColaboradorProyectoSerializer

class ColaboradorDetailView(generics.RetrieveAPIView) :
    queryset = Colaborador.objects.all()
    serializer_class =  serializers.ColaboradorDetailSerializer