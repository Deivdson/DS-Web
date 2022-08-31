from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

class Simulado(models.Model):
    titulo = models.CharField('titulo', max_length=20)
    descricao = models.CharField(max_length=50)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class Questao(models.Model):
    texto = models.TextField('texto')
    valor = models.IntegerField(default=0)
    simulado = models.ForeignKey(Simulado, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = 'Questões'

    def __str__(self):
        return self.texto

class Alternativa(models.Model):
    texto = models.TextField('texto')
    questao = models.ForeignKey(Questao, on_delete = models.CASCADE)
    correta = models.BooleanField(default = False)

    def __str__(self):
        return self.texto

class Resposta(models.Model):
    texto = models.TextField('texto')
    questao = models.ForeignKey(Questao, on_delete = models.CASCADE)

    def __str__(self):
        return self.texto