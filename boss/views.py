from django.shortcuts import render
from api.models import *

# Create your views here.
def index(request):
	context = {}
	context['pagina'] = 'index'

	return render(request, 'boss/index.html', context)


def login(request):
	context = {}
	context['pagina'] = 'login'

	return render(request, 'boss/login.html', context )


def reportes(request):
	context = {}
	context['pagina'] = 'reportes'

	return render(request, 'boss/reportes.html', context )


def estudiantes(request):
	context = {}
	context['pagina'] = 'estudiantes'
	lista_estudiantes = Estudiante.objects.all()
	context['listaEstudiantes'] = lista_estudiantes
	print(lista_estudiantes)

	return render(request, 'boss/estudiantes.html', context )


def profesores(request):
	context = {}
	context['pagina'] = 'profesor'

	return render(request, 'boss/profesores.html', context )


def cursos(request):
	context = {}
	context['pagina'] = 'cursos'

	return render(request, 'boss/cursos.html',  context )


def configuracion(request):
	context = {}
	context['pagina'] = 'configuracion'

	return render(request, 'boss/configuracion.html', context )
