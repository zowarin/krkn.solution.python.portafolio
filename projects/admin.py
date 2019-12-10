from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Puesto)
admin.site.register(Tecnologia)
admin.site.register(Archivo)
admin.site.register(Colaborador)
admin.site.register(Galeria)
admin.site.register(Image)
# admin.site.register(RolProyecto)
admin.site.register(ColaboradorProyecto)
admin.site.register(Educacion)
