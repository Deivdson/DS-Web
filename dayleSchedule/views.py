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
        elif request.POST['privado']:
            ## Cronograma privado possui 'privacidade' = false
            cronograma = Cronograma(titulo=titulo_cronograma, data_inicio=inicio, data_fim=fim, privacidade=False, aluno = aluno)
            cronograma.save()

        if request.POST['titulo_materia_1']:
            #i = 1
            #name = 'titulo_materia_'
            #while request.POST[f'{name}{i}'] != None:
                #materia = Tarefa(titulo=request.POST['titulo_materia_'+str(i)], assunto=request.POST['assunto_'+str(i)],
                #descricao = request.POST['descricao_'+str(i)], hora_inicio=request.POST['horario_inicio_'+str(i)],
                #hora_fim=request.POST['horario_fim_'+str(i)], data=request.POST['data_materia_'+str(i)], cronograma = cronograma)
                #materia.save()
                #i=i+1
            materia = Tarefa(titulo=request.POST['titulo_materia_1'], assunto=request.POST['assunto_1'],
            descricao = request.POST['descricao_1'], hora_inicio=request.POST['horario_inicio_1'],
            hora_fim=request.POST['horario_fim_1'], data=request.POST['data_materia_1'], cronograma = cronograma)
            materia.save()

        if request.POST['titulo_materia_2']:
            materia = Tarefa(titulo=request.POST['titulo_materia_2'], assunto=request.POST['assunto_2'],
            descricao = request.POST['descricao_2'], hora_inicio=request.POST['horario_inicio_2'],
            hora_fim=request.POST['horario_fim_2'], data=request.POST['data_materia_2'], cronograma = cronograma)
            materia.save()


        #cronograma.tarefa.add(materia)
        #cronograma.save()

        return render(request, 'dayleSchedule/detalhes.html', {'cronograma':cronograma})
        ##return HttpResponseRedirect(reverse('dayleSchedule:index'))






