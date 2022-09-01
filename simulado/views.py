from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Simulado, Questao, Resposta, Usuario, Alternativa
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
class index(View):
    def get(self,request,*args,**kwargs):
        simulados = Simulado.objects.all()
        return render(request, 'simulado/index.html', {'simulados':simulados})

class cadastro(View):
    def get(self,request,*args,**kwargs):
        return render(request,'simulado/cadastro.html')

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        nome = request.POST['nome']
        senha = request.POST['senha']

        user = User.objects.create_user(username, 'email', senha)
        user.first_name = nome
        user.save()
        simulados = Simulado.objects.all()
        return render(request, 'simulado/index.html', {'simulados':simulados, 'msg':'sucesso'})

@method_decorator(
    login_required(login_url='/simulado/login'), name='dispatch'
)
class formSimulado(View):
    def get(self, request,*args,**kwargs):
        return render(request,'simulado/formSimulado.html')

    def post(self, request,*args,**kwargs):
        ts = request.POST['titulo']
        desc = request.POST['descricao']
        simulado = Simulado(titulo = ts, descricao = desc)
        simulado.save()

        tq1 = request.POST['titulo_questao1']
        tq2 = request.POST['titulo_questao2']
        q1 = Questao(texto=tq1, simulado = simulado, valor=request.POST['valor_q1'])
        q2 = Questao(texto=tq2, simulado = simulado, valor=request.POST['valor_q2'])

        q1.save()
        q2.save()

        q1_alt1 = Alternativa(texto = request.POST['q1_alt1'], questao = q1)
        q1_alt1.save()
        q1_alt2 = Alternativa(texto = request.POST['q1_alt2'], questao = q1)
        q1_alt2.save()
        q2_alt1 = Alternativa(texto = request.POST['q2_alt1'], questao = q2)
        q2_alt1.save()
        q2_alt2 = Alternativa(texto = request.POST['q2_alt2'], questao = q2)
        q2_alt2.save()

        if request.POST['q1_alt3']:
            q1_alt3 = Alternativa(texto = request.POST['q1_alt3'], questao = q1)
            q1_alt3.save()
        if request.POST['q1_alt4']:
            q1_alt4 = Alternativa(texto = request.POST['q1_alt4'], questao = q1)
            q1_alt4.save()
        if request.POST['q2_alt3']:
            q2_alt3 = Alternativa(texto = request.POST['q2_alt3'], questao = q2)
            q2_alt3.save()
        if request.POST['q2_alt4']:
            q2_alt4 = Alternativa(texto = request.POST['q2_alt4'], questao = q2)
            q2_alt4.save()
        resposta1 = Resposta(texto = request.POST['resposta_q1'], questao=q1)
        resposta2 = Resposta(texto = request.POST['resposta_q2'], questao=q2)
        resposta1.save()
        resposta2.save()

        alternativas = request.POST.getlist('alt_q1')
        for alt in alternativas:
            if alt=='q1_alt1':
                alternativa = get_object_or_404(pk='q1_alt1')
                alternativa.correta=True
            if alt=='q1_alt2':
                alternativa = get_object_or_404(pk='q1_alt2')
                alternativa.correta=True
            if alt=='q1_alt3':
                alternativa = get_object_or_404(pk='q1_alt3')
                alternativa.correta=True
            if alt=='q1_alt4':
                alternativa = get_object_or_404(pk='q1_alt4')
                alternativa.correta=True

        alternativas = request.POST.getlist('alt_q2')
        for alt in alternativas:
            if alt=='q2_alt1':
                alternativa = get_object_or_404(pk='q2_alt1')
                alternativa.correta=True
            if alt=='q2_alt2':
                alternativa = get_object_or_404(pk='q2_alt2')
                alternativa.correta=True
            if alt=='q2_alt3':
                alternativa = get_object_or_404(pk='q2_alt3')
                alternativa.correta=True
            if alt=='q2_alt4':
                alternativa = get_object_or_404(pk='q2_alt4')
                alternativa.correta=True

        simulados = Simulado.objects.all()
        return render(request, 'simulado/index.html',{'simulados':simulados})
        #return HttpResponseRedirect(reverse('simulado:index'))

class detalhes(View):
    def get(self,request,*args,**kwargs):
        simulado = get_object_or_404(Simulado, pk= kwargs['pk'])
        return render(request, 'simulado/detalhes.html',{'simulado':simulado})

class resultado(View):
    def get(self, request, *args, **kwargs):
        simulado = get_object_or_404(Simulado, pk= kwargs['pk'])
        return render(request, 'simulado/resultado.html',{'simulado':simulado})

@method_decorator(
    login_required(login_url='/simulado/login'), name='dispatch'
)
class iniciarSimulado(View):
    def get(self,request,*args,**kwargs):
        simulado = get_object_or_404(Simulado, pk= kwargs['pk'])
        request.session['id_simulado']=kwargs['pk']
        return render(request, 'simulado/iniciarSimulado.html',{'simulado':simulado})

    def post(self, request, *args, **kwargs):
        simulado = get_object_or_404(Simulado, pk= request.session['id_simulado'])
        del request.session['id_simulado']
        questoes = Questao.objects.all().filter(simulado = simulado)

        # pontuacao = 0
        for q in questoes:
            #correta = Alternativa.objects.all().filter(correta=True).filter(questao=q)
            #alternativas = request.POST.getlist(q.id)
            id_alt = request.POST[q.id]
            alt = get_object_or_404(Alternativa,pk=id_alt)
            if alt.correta:
                pontuacao += q.valor
            #for id in alternativas:
            #    alt = get_object_or_404(Alternativa,pk=id)
            #    if alt.correta:
            #        simulado.pontuacao+=q.valor
            #        simulado.save()

#            id_alt = request.POST[q.id]
#            selecionada = get_object_or_404(Alternativa, pk=id_alt)
#            if selecionada:
#                if selecionada.correta:
#                        simulado.pontuacao+=q.valor
#                        simulado.save()
#            else:
#                contexto = {
#                    'simulado': simulado,
#                    'msg_erro': 'Selecione uma alternativa!'
#                }
#                return render(request,'simulado/detalhes.html',contexto)
#
#        return HttpResponseRedirect(
#            reverse('simulado:resultado',  args=(simulado.id,))
#        )
       #retornar resultado
        return render(request, 'simulado/resultado.html',{'simulado':simulado,'pontuacao':pontuacao})

#####
#class VotacaoView(View):
#    def post(self, request, *args, **kwargs):
#        id_pergunta = kwargs['pk']
#        pergunta = get_object_or_404(Pergunta, pk = id_pergunta)
#        try:
#            id_opcao = request.POST['alternativa']
#            selecionada = pergunta.alternativa_set.get(pk = id_opcao)
#        except (KeyError, Alternativa.DoesNotExist):
#            contexto = {
#                'pergunta': pergunta,
#                'msg_erro': 'Selecione uma opção válida!'
#            }
#            return render(request, 'enquetes/detalhes.html', contexto)
#        else:
#            selecionada.quant_votos += 1
#            selecionada.save()
#            return HttpResponseRedirect(
#                reverse('enquetes:resultado', args=(pergunta.id,))
#            )
#####