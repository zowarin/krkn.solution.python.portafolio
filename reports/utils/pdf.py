from django.template.loader import render_to_string
# PDF Library
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
# PDF
class PdfGeneratorProject():

    def __init__(self, base_url='', font_config=FontConfiguration()):
        self.base_url = base_url
        self.css_string = '@page{ size:A4; margin: 2cm;}'
        self.font_config = font_config

    def get_portada_project(self, project, template_name='projects/pdf/proyecto_portada.html'):
        return self.get_document_pdf(template_name, css_string=self.css_string , context ={'project': project})

    def get_contenido_project(self, project, template_name='projects/pdf/proyecto_contenido.html'):
        return self.get_document_pdf(template_name, css_string=self.css_string , context ={'project': project})

    def get_contraportada_project(self, project, template_name='projects/pdf/proyecto_contraportada.html'):
        return self.get_document_pdf(template_name, css_string=self.css_string , context ={'project': project})

    def get_pdf_project(self, project, response):
        documents = []
        documents.append(self.get_portada_project(project))
        documents.append(self.get_contenido_project(project))
        documents.append(self.get_contraportada_project(project))
        all_pages = [page for document in documents for page in document.pages]
        documents[0].copy(all_pages).write_pdf(response)

    def get_document_pdf(self, template_name, css_string , context):
        # pdf
        html_string = render_to_string(template_name, context)
        css = CSS(string=css_string)
        document = HTML(
            string=html_string,
            base_url=self.base_url
        ).render(
            font_config=self.font_config,
            stylesheets=[css]
        )
        return document

    def get_portada_portafolio(self, projects, template_name='projects/pdf/portada_portafolio.html'):
        return self.get_document_pdf(template_name, css_string=self.css_string , context ={'projects': projects})

    def get_contraportada_portafolio(self, projects, template_name='projects/pdf/contraportada_portafolio.html'):
        return self.get_document_pdf(template_name, css_string=self.css_string , context ={'projects': projects})

    def get_pdf_portafolio(self , projects, response):
        documents = []
        documents.append(self.get_portada_portafolio(projects))
        for project in projects :
            documents.append(self.get_portada_project(project))
            documents.append(self.get_contenido_project(project))
        documents.append(self.get_contraportada_portafolio(projects))
        all_pages = [page for document in documents for page in document.pages]
        documents[0].copy(all_pages).write_pdf(response)
