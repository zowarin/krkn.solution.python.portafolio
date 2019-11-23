from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
# PDF Library
from weasyprint import HTML, CSS, default_url_fetcher
from weasyprint.fonts import FontConfiguration
import logging
# PDF
class PdfGeneratorProject():

    def __init__(self, base_url=''):
        self.base_url = base_url
        self.css_string = ''
        self.font_config = FontConfiguration()
        logger = logging.getLogger('weasyprint')
        logger.addHandler(logging.FileHandler('weasyprint.log')) 

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
        css = CSS(
            string=css_string , 
            font_config=self.font_config ,
            url_fetcher=self.my_fetcher_css
        )
        font_config = FontConfiguration()
        document = HTML(
            string=html_string,
            base_url=self.base_url,
            url_fetcher=self.my_fetcher_html,
        ).render(
            font_config=self.font_config,
            stylesheets=[
                css 
            ]
        )
        return document

    def my_fetcher_css(self, url, timeout=10, ssl_context=None):
        # print(f'my_fetcher_css  -->> {url}')
        return default_url_fetcher(url, timeout, ssl_context)
    
    def my_fetcher_html(self, url, timeout=10, ssl_context=None):
        # print(f'my_fetcher_html  -->> {url}')
        return default_url_fetcher(url, timeout, ssl_context)

    def get_portada_portafolio(self, projects, template_name='projects/pdf/portafolio_portada.html'):
        return self.get_document_pdf(template_name, css_string=self.css_string , context ={'projects': projects})

    def get_contenido_portafolio(self, projects, template_name='projects/pdf/portafolio_contenido.html'):
        return self.get_document_pdf(template_name, css_string=self.css_string , context ={'projects': projects , 'range': range(10)})

    def get_contraportada_portafolio(self, projects, template_name='projects/pdf/portafolio_contraportada.html'):
        return self.get_document_pdf(template_name, css_string=self.css_string , context ={'projects': projects})

    def get_pdf_portafolio(self , projects, response):
        documents = []
        # documents.append(self.get_portada_portafolio(projects))
        documents.append(self.get_contenido_portafolio(projects))
        # for project in projects :
        #     documents.append(self.get_portada_project(project))
        #     documents.append(self.get_contenido_project(project))
        # documents.append(self.get_contraportada_portafolio(projects))
        all_pages = [page for document in documents for page in document.pages]
        documents[0].copy(all_pages).write_pdf(response)
