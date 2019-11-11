from django.urls import path
from . import views


urlpatterns = [
    path('projects/' , views.projects, name='projects') ,
    path('projects/<int:pk>' , views.projects_detail, name='projects_detail') ,
]
