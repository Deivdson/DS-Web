from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Simulado, Questao, Resposta, Usuario
from django.urls import reverse

# Create your views here.

class index(View):
    def get(self,request,*args,**kwargs):
        simulados = Simulado.object.all()
        return render(request, 'simulado/index.html', {'simulados':simulados})

class cadastro(View):
    def get(self,request,*args,**kwargs):
        return render(request,'simulado/cadastro.html')

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        nome = resquest.POST['nome']
        senha = request.POST['senha']

        user = User.objects.creat_user(username, 'email', senha, nome)
        user.save
        simulados = Simulado.object.all()
        return render(request, 'simulado/index.html', {'simulados':simulados, 'msg':'sucesso'})