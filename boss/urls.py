from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    path('', index, name='index'),
    path('login', login, name='login'),
    path('reportes', reportes, name='reportes'),
    path('estudiantes/<str:msj>', estudiantes, name='estudiantes'),
    path('profesores', profesores, name='profesores'),
    path('cursos', cursos, name='cursos'),
    path('configuracion', configuracion, name='configuracion'),
    path('crear-estudiante', crear_estudiante, name='nuevoEstudiante'),
    path('test', test, name='test'),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)

