from ..models import *
from rest_framework import serializers

class ColaboradorProyectoSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Colaborador
        fields = ('id' , 'nombre')



class RolProyectoSerializer(serializers.ModelSerializer) : 
    puesto = serializers.StringRelatedField()
    colaborador = ColaboradorProyectoSerializer(many = False)
    class Meta:
        model = RolProyecto
        fields = ('descripcion' , 'puesto' , 'colaborador')


class ImageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Image
        fields = ('nombre' , 'alt' , 'image')


class GaleriaSerializer(serializers.ModelSerializer) : 
    images = ImageSerializer(many = True)
    class Meta:
        model = Galeria
        fields = ('nombre' , 'images')


class ArchivoSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Archivo
        fields = ('nombre' , 'descripcion' , 'url' , 'tipo')


class TecnologiaSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Tecnologia
        fields = '__all__' 


class ClienteSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Cliente 
        fields = ('nombre' , 'web_page')


class ProyectoSerializer(serializers.ModelSerializer) :
    cliente = ClienteSerializer( many = False , read_only = True)
    tecnologias = TecnologiaSerializer(many = True)
    class Meta:
        model = Proyecto
        fields = (
            'id' , 
            'nombre' , 
            'descripcion' , 
            'fecha_inicio' , 
            'fecha_fin' , 
            'tecnologias' , 
            'cliente' , 
        )


class ProyectoDetailSerializer(ProyectoSerializer) :
    archivos = ArchivoSerializer(many = True)
    galerias = GaleriaSerializer(many = True)
    colaboradores = RolProyectoSerializer(many = True)
    class Meta:
        model = Proyecto
        fields = (
            'id' , 
            'nombre' , 
            'decripcion' , 
            'fecha_inicio' , 
            'fecha_fin' , 
            'tecnologias' , 
            'cliente' , 
            'archivos' ,
            'galerias' ,
            'colaboradores'
        )


class ColaboradorRolProyectoSerializer(serializers.ModelSerializer) :
    puesto = serializers.StringRelatedField()
    proyecto = ProyectoSerializer(many = False)
    class Meta:
        model = RolProyecto
        fields = ('descripcion' , 'proyecto' , 'puesto')

class PerfilLinkedSerializar(serializers.Serializer) :
    nombre = serializers.CharField(max_length=200)


class ColaboradorDetailSerializer(ColaboradorProyectoSerializer) :
    rol_proyecto = ColaboradorRolProyectoSerializer(many = True)
    perfil = PerfilLinkedSerializar()
    class Meta:
        model = Colaborador
        fields = ('id' , 'nombre' , 'rol_proyecto' , 'perfil')