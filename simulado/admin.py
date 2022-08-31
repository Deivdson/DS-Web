from django.contrib import admin

from .models import Usuario, Simulado, Questao, Resposta, Alternativa

admin.site.register(Usuario)
admin.site.register(Simulado)
admin.site.register(Questao)
admin.site.register(Resposta)
admin.site.register(Alternativa)
# Register your models here.
