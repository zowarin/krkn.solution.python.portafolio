from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from django.shortcuts import get_object_or_404
# Model's
from projects.models import Proyecto
# Utils PDF
from .utils.pdf import PdfGeneratorProject

def projects(request):
    projects = Proyecto.objects.all()
    # file
    file_name = f'krkn.solution - portafolio.pdf'
    # response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{file_name}"'
    # PDF
    base_url = 'http://127.0.0.1:5000/' # TODO !!!!!
    pdf_generator = PdfGeneratorProject(base_url=base_url)
    pdf_generator.get_pdf_portafolio(projects, response)
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


