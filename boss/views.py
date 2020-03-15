from django.shortcuts import render
from api.models import *
from django.http import HttpResponse
import random
from django.contrib.auth.models import User
from django.shortcuts import redirect


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


def estudiantes(request, msj):
	context = {}
	context['pagina'] = 'estudiantes'
	context['msj'] = msj
	lista_estudiantes = Estudiante.objects.all()
	context['listaEstudiantes'] = lista_estudiantes
	print(lista_estudiantes)

	return render(request, 'boss/estudiantes.html', context )


def crear_estudiante(request):
	context = {}
	if request.method == 'POST':
		try:
			data = request.POST
			print(data.get('nombre'))
			
			user = User.objects.create_user(
				username = data.get('nombre') + " " + data.get('apellido'),
				password = "Corona!*" + str(random.randrange(0, 60)),
				email = data.get('email')
			)
			user.save( )

			estudiante = Estudiante(
				usuario = user,
				codigo = data.get('matricula'),
				matricula = data.get('matricula'),
				carrera = data.get('carrera')
				)
			estudiante.save()

			print("Hola mis perros")
			msj = "exito"
		except:
			msj = "error"

	return redirect('estudiantes', msj=msj)


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



#BORRAR LUEGO
def test(request):
	numero_aleatorio = random.randrange(0, 60)
	return HttpResponse("Hola mis perros")