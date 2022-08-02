from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario

class Cronograma(models.Model):
    privacidade = models.BooleanField()
    data_inicio = models.DateTimeField('Data inicio Cronograma', default=timezone.now)
    data_fim = models.DateTimeField('Data fim Cronograma', default=timezone.now)
    titulo = models.CharField(max_length=100, default='Novo Cronograma')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    class Meta:
        verbose_name='Cronograma'
    def __str__(self):
        return ("{0} - {1}").format(self.titulo, self.aluno)

class Tarefa(models.Model):
    titulo = models.CharField(max_length=50, default = 'Nova Tarefa')
    assunto = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, default='Sem tipo')
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fim = models.TimeField(null=True)
    data = models.DateTimeField('Data Cronograma')
    status = models.BooleanField(default=False)
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE)

    def desta_semana(self):
        return(
            (self.data >= self.cronograma.data_inicio) and
            (self.data <= self.cronograma.data_fim)
        )

    def __str__(self):
        return self.descricao

class Tipo(models.Model):
    nome = models.CharField(max_length=12)

    def __str__(self):
        return self.nome







