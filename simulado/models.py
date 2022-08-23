from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        self.username

class Simulado(models.Model):
    titulo = models.CharField('título', max_length=20)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        self.titulo

class Questao(models.Model):
    texto = models.TextField()
    simulado = models.ForeignKey(Simulado, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = 'Questões'

    def __str__(self):
        self.texto

class Resposta(models.Model):
    texto = models.TextField('texto')
    questao = models.ForeignKey(Questao, on_delete = models.CASCADE)

    def __str__(self):
        self.texto