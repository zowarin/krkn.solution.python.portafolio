from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from .models import *

class TextFieldMarkdown(admin.ModelAdmin) :
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }


# Register your models here.



admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Puesto)
admin.site.register(Tecnologia)
admin.site.register(Archivo)
admin.site.register(Colaborador , TextFieldMarkdown)
admin.site.register(Galeria)
admin.site.register(Image)
admin.site.register(ColaboradorProyecto , TextFieldMarkdown)
admin.site.register(ColaboradorCliente , TextFieldMarkdown)
admin.site.register(Educacion)


