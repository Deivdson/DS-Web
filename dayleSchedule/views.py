from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Cronograma, Aluno, Tarefa

def index(request):
    latest_ds_list = Cronograma.objects.order_by('-data_inicio')
    context = {'latest_ds_list': latest_ds_list}
    return render(request, 'dayleSchedule/index.html', context)

def detalhes(request, pk):
    cronograma = get_object_or_404(Cronograma, pk=pk)
    return render(request, 'dayleSchedule/detalhes.html',{'cronograma':cronograma})

class cronogramaForm(View):
    def get(self, request, *args, **kwargs):
        alunos = Aluno.objects.order_by('nome')
        return render(request, 'dayleSchedule/cronogramaForm.html', {'alunos':alunos})

    def post(self, request,  *args, **kwargs):
        titulo_cronograma = request.POST['titulo_cronograma']
        inicio = request.POST['inicio']
        fim = request.POST['fim']
        ##aluno = Aluno.objects.get(usuario='Paulo23')
        aluno = get_object_or_404(Aluno, usuario='Paulo23')
        if request.POST['publico']:
            ## Cronograma público possui 'privacidade' = true
            cronograma = Cronograma(titulo=titulo_cronograma, data_inicio=inicio, data_fim=fim, privacidade=True, aluno = aluno)
            cronograma.save()
        else:
            ## Cronograma privado possui 'privacidade' = false
            cronograma = Cronograma(titulo=titulo_cronograma, data_inicio=inicio, data_fim=fim, privacidade=False, aluno = aluno)
            cronograma.save()

        #if request.POST['titulo_materia']:
        materia = Tarefa(titulo=request.POST['titulo_materia'], assunto=request.POST['assunto'],
        descricao = request.POST['descricao'], hora_inicio=request.POST['horario_inicio'],
        hora_fim=request.POST['horario_fim'], data=request.POST['data_materia'], cronograma = cronograma)
        materia.save()
        #cronograma.tarefa.add(materia)
        #cronograma.save()

        return render(request, 'dayleSchedule/detalhes.html', {'cronograma':cronograma})
        ##return HttpResponseRedirect(reverse('dayleSchedule:index'))






