from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	cedula = models.CharField(max_length=255, blank=False, unique=True)
	def __str__(self):
		return "{} ".format(self.usuario)

class Estudiante(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	codigo = models.CharField(max_length=255, blank=False, unique=True)
	matricula = models.CharField(max_length=255, blank=False, unique=True)
	carrera = models.CharField(max_length=255, blank=False, unique=True)
	def __str__(self):
		return "{} ".format(self.usuario)

class Aula(models.Model):
	nombre = models.CharField(max_length=255, blank=False)
	def __str__(self):
		return "{} ".format(self.nombre)

class Cursos(models.Model):
	aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
	codigo = models.CharField(max_length=255, blank=False)
	profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
	nombre_de_curso = models.CharField(max_length=255, blank=False)
	def __str__(self):
		return "{} ".format(self.nombre_de_curso)

class Horarios(models.Model):
	DIAS = [
        ('L', 'Lunes'),
        ('M', 'Martes'),	
        ('I', 'Miercoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes')
    ]
	dia = models.CharField( max_length=1, choices=DIAS, default='L')
	hora_inicio = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	hora_fin = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

	def __str__(self):
		return "{} ".format(self.dia)

class Clases(models.Model):
	curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
	horario = models.ForeignKey(Horarios, on_delete=models.CASCADE)
	ESTADO = [
			('A','Activo'),
			('N','No Activo')
	]
	status = models.CharField( max_length=1, choices=ESTADO, default='N')
	def __str__(self):
		return "{} ".format(self.curso)

class Lista_de_Estudiantes(models.Model):
	estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
	def __str__(self):
		return "{} {} ".format(self.curso, self.estudiante)

class Asistencia(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	hora_inicio = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	hora_fin = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	def __str__(self):
		return "{} ".format(self.usuario)

class Tabla_test(models.Model):
    columna_uno = models.CharField(max_length=200)
    columna_dos = models.CharField(max_length=200)
    columna_tres = models.CharField(max_length=200)
    columna_cuatro = models.CharField(max_length=200)