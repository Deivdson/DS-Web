from django.contrib import admin

from .models import Usuario, Simulado, Questao, Resposta

admin.site.register(Usuario)
admin.site.register(Simulado)
admin.site.register(Questao)
admin.site.register(Resposta)
# Register your models here.
