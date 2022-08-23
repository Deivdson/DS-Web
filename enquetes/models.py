from django.db import models
from django.utils import timezone
import datetime


class Rotulo(models.Model):
    titulo = models.CharField('título', max_length = 30)
    class Meta:
        verbose_name = 'Rótulo'
    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    descricao = models.TextField('descrição')
    naturalidade = models.CharField(max_length = 30)
    data_nasc = models.DateField('Data de nascimento')
    generos = models.CharField('Gênero literário', max_length = 30)
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name_plural = 'Perfis'

class Autor(models.Model):
    pseudonimo = models.CharField(max_length = 200, default = 'null')
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    def __strs__(self):
        return self.descricao
    class Meta:
        verbose_name_plural = 'Autores'

class Pergunta(models.Model):
    texto = models.CharField(max_length = 200)
    imagem = models.ImageField(
        upload_to='perguntas', null=True, blank=True
        )
    data_pub = models.DateTimeField('Data de publicação')
    data_fim = models.DateField('Data de encerramento', null=True)
    autor = models.ForeignKey(
        Autor, on_delete = models.CASCADE, null=True
    )
    rotulos = models.ManyToManyField(Rotulo, blank=True)
    possui_resposta = models.BooleanField(default=False)

    def _str_(self):
        return ("{0} - {1}").format(self.id, self.texto)

    def publicada_recentemente(self):
        now = timezone.now()
        delta_24hs = datetime.timedelta(hours=24)
        return(
            (self.data_pub <= now) and
            (self.data_pub >=now - delta_24hs)
        )
    publicada_recentemente.admin_order_field = 'data_pub'
    publicada_recentemente.boolean = True
    publicada_recentemente.short_description = 'Recente?'



class Alternativa(models.Model):
    texto = models.CharField(max_length = 50)
    quant_votos = models.IntegerField(
        'Quantidade de votos', default = 0
    )
    pergunta = models.ForeignKey(
        Pergunta, on_delete = models.CASCADE
    )
    correta = models.BooleanField(default = False)

    def _str_(self):
        return self.texto

class Usuario(models.Model):
    login = models.CharField(max_length = 25)
    senha = models.CharField(max_length = 25)

    class Meta:
        verbose_name = 'usuário'
    def __str__(self):
        return self.login

class  Voto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)










