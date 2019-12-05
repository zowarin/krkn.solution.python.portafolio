from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views import generic
# Model's
from projects.models import Proyecto , Tecnologia
# Utils PDF
from .utils.pdf import PdfGeneratorProject

def projects(request):
    projects = Proyecto.objects.all()
    tecnologys = Tecnologia.objects.all()
    # file
    file_name = f'krkn.solution - portafolio.pdf'
    # response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{file_name}"'
    response['Content-Transfer-Encoding'] = 'binary'
    # PDF
    base_url = 'http://127.0.0.1:5000/' # TODO !!!!!
    pdf_generator = PdfGeneratorProject(base_url=base_url)
    
    context = {
        'title' : 'Portafolio' , 
        'sub_title' : 'krkn.solutions' , 
        'contacto' : 'contacto@krkn.solutions' ,
        'telefono' : '+52 442 181 26 33' ,
        'web_site' : 'http://krkn.solutions/' , 
        'ciudad' : 'Queretaro, Qro.' ,
        'pais' : 'México' ,

        'chapters' : [
            {
                'chapter_title' : 'Release the Developer' ,
                'sections' : [
                    {
                        'title' : 'Proyectos' ,
                        'sub_title' : 'Algunos de nuestros proyectos:' ,
                        'id' : 'proyectos' ,
                        'items' : projects ,
                        'class' : 'columns-2' ,
                    } ,
                    {
                        'title' : 'Tecnologías' ,
                        'sub_title' : 'Herramientas con las que trabajo:' ,
                        'id' : 'tecnologias' ,
                        'items' : tecnologys ,
                        'class' : 'columns-3' ,
                    } ,
                ]
            } , 
        ] ,

        'cover' : True ,
        'contents' : True ,
        'range': range(10) ,
    }

    print(context)
    
    pdf_generator.get_pdf_portafolio(
        context = context ,
        response = response , 
    )
    return response

def projects_detail(request , pk):
    # template
    project = get_object_or_404(Proyecto, pk=pk)
    # file
    file_name = f'krkn.solution - {project.nombre}.pdf'
    # response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{file_name}"'
    # PDF
    base_url = 'http://127.0.0.1:5000/' # TODO !!!!!
    pdf_generator = PdfGeneratorProject(base_url=base_url)
    pdf_generator.get_pdf_project(project, response)
    return response


class IndexView(generic.ListView):
    context_object_name = 'projects'
    template_name = 'projects/pdf/portafolio_contenido.html'
    def get_queryset(self):
        return Proyecto.objects.all()
