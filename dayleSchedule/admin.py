from django.contrib import admin

from .models import Cronograma, Tarefa, Aluno
# Register your models here.

admin.site.register(Cronograma)
admin.site.register(Tarefa)
admin.site.register(Aluno)
