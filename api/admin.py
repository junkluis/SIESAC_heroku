from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Aula)
admin.site.register(Cursos)
admin.site.register(Clases)
admin.site.register(Horarios)
admin.site.register(Lista_de_Estudiantes)
admin.site.register(Asistencia)