from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey , GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now



# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    web_page = models.URLField(
        max_length=200 ,
        null = True ,
        blank = True ,
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cliente_krkn'


class Tecnologia(models.Model) :
    nombre = models.CharField(max_length=200)
    url = models.URLField(
        max_length=200 ,
        null = True ,
        blank = True ,
    )
    logotipo = models.URLField(
        max_length=200 ,
        null = True ,
        blank = True ,
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'proyecto_krkn_tecnologia'


class Proyecto(models.Model):
    cliente = models.ForeignKey(
        Cliente , 
        on_delete=models.SET_NULL , 
        null = True ,
        blank = True ,
        related_name="cliente" ,
        related_query_name="cliente" ,
    )
    nombre = models.CharField(
        max_length=200
    )
    descripcion = models.TextField(
        null = True ,
        blank = True , 
    )
    ciudad =  models.CharField(
        max_length=200 ,
        blank= True , 
    )
    activo =  models.BooleanField(
        default =  False
    )
    created = models.DateTimeField(
        default=now, 
        editable=False
    )
    fecha_inicio = models.DateField(
        default = now
    )
    fecha_fin = models.DateField(
        null = True ,
        blank = True , 
    )
    tecnologias = models.ManyToManyField(Tecnologia)
    
    @property
    def year(self) :
        return 2019



    def __str__(self):
        return self.nombre


    class Meta:
        db_table = 'proyecto_krkn'
        ordering = ['-fecha_inicio']
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        

class Archivo(models.Model) :

    REPOSITORIO = 'Repositorio'
    AVANCE = 'Avance'
    INFORME = 'Informe'
    ARTICULO = 'Artículo'
    VIDEO = 'Video'
    OTRO = 'Otro'

    TIPO_ARCHIVO_CHOISE = (
        (REPOSITORIO , 'Repositorio') ,
        (AVANCE , 'Avance') ,
        (INFORME , 'Informe') ,
        (ARTICULO , 'Artículo') ,
        (VIDEO , 'Video') ,
        (OTRO , 'Otro') ,
    )

    proyecto = models.ForeignKey(
        Proyecto ,
        related_name= 'archivos' ,
        on_delete=models.CASCADE ,
    )
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(
        null = True , 
        blank = True ,
    )
    url = models.URLField(
        max_length=200 ,
        null = False
    )
    tipo = models.CharField(
        max_length = 50,
        choices = TIPO_ARCHIVO_CHOISE,
        default = REPOSITORIO,
    )

    created = models.DateTimeField(
        default = now, 
        editable = False 
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'proyecto_krkn_archivo'


class Galeria(models.Model) :
    proyecto = models.ForeignKey(
        Proyecto ,
        related_name= 'galerias' ,
        on_delete=models.CASCADE ,
    )
    nombre = models.CharField(max_length=200)
    created = models.DateTimeField(
        default = now, 
        editable = False 
    )
    
    def __str__(self):
        return f'{self.proyecto.nombre} | {self.nombre}'
    
    class Meta:
        db_table = 'proyecto_krkn_galeria'
        ordering = ['-created']


class Image(models.Model) :
    galeria = models.ForeignKey(
        Galeria ,
        related_name= 'images' ,
        on_delete=models.CASCADE ,
        null = True
    )
    nombre = models.CharField(max_length=200)
    alt = models.CharField(max_length=50)
    src =  models.ImageField(
        upload_to='projects/images/',
        null = True , 
        blank = True ,
    )
    created = models.DateTimeField(
        default = now, 
        editable = False 
    )

    
    def __str__(self):
        return f'{self.galeria.nombre} | {self.nombre}'
    
    class Meta:
        db_table = 'proyecto_krkn_imagen_galeria'
        ordering = ['-created']


class Puesto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(
        null = True , 
        blank = True ,
    )

    def __str__(self):
        return f'{self.nombre}'

    class Meta: 
        db_table = 'puesto_krkn'


class Colaborador(models.Model) :
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'colaborador_krkn'
    


class RolProyecto(models.Model) :
    proyecto = models.ForeignKey(
        Proyecto ,
        related_name= 'colaboradores' ,
        on_delete=models.CASCADE ,
        # null = True
    ) 

    puesto = models.ForeignKey(
        Puesto ,
        # related_name= 'actividad' ,
        on_delete=models.CASCADE ,
        # null = True 
    ) 

    colaborador = models.ForeignKey(
        Colaborador ,
        related_name= 'rol_proyecto' ,
        on_delete=models.CASCADE ,
        # null = True
    ) 
    
    
    descripcion = models.CharField(max_length=200)
    created = models.DateTimeField(
        default = now, 
        editable = False 
    )

    def __str__(self) :
        return f'{self.proyecto.nombre} | {self.puesto.nombre} | {self.colaborador.nombre} | {self.descripcion}'

    class Meta:
        db_table = 'proyecto_krkn_rol'
        ordering = ['-created']
        unique_together = ('proyecto' , 'puesto' ,'colaborador')
    