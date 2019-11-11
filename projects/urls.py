from django.urls import path
from .api import views


urlpatterns = [
    path('projects' , views.ProyectoListView.as_view(), name=None) ,
    path('projects/<int:pk>' , views.ProyectoDetailView.as_view(), name=None) ,
    path('clients' , views.ClienteListView.as_view(), name=None) ,
    path('technologies' , views.TecnologiasListView.as_view(), name=None) ,
    path('collaborator' , views.ColaboradorListView.as_view(), name=None) ,
    path('collaborator/<int:pk>' , views.ColaboradorDetailView.as_view(), name=None) ,
]