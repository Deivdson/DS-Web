from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#from django.template  import loader
from .models import Pergunta, Alternativa

# Create your views here.
class IndexView(generic.ListView):

    template_name = 'enquetes/index.html'
    context_object_name = 'ultima_listaq'

    def get_queryset(self):
        return Pergunta.objects.filter(data_pub__lte=timezone.now())[:25]

    #lista_enquetes = Pergunta.objects.order_by('data_pub')[:25]
    #contexto = {'lista_enquetes' : lista_enquetes}
    ##resposta = '<br><br>'.join(enq.texto for enq in lista_enquetes)
    #return render(request, 'enquetes/index.html', contexto)


class DetalhesView(generic.DetailView):
    model = Pergunta
    #template_name = 'enquetes/detalhes.html'

    #pergunta = get_object_or_404(Pergunta, pk = pk)
    #return render(request, 'enquetes/detalhes.html', {'pergunta':pergunta})


class ResultadosView(generic.DetailView):
    model = Pergunta
    template_name = 'enquetes/resultados.html'


def votacao(request, id_enquete):

    pergunta = get_object_or_404(Pergunta, pk=id_enquete)
    try:
        selecionada = pergunta.alternativa_set.get(pk=request.POST['alternativa'])
    except (KeyError, Alternativa.DoesNotExist):
        return render(request, 'enquetes/detalhes.html', {
            'pergunta':pergunta,
            'error_message':'Você não selecionou uma opção'})
    else:
        selecionada.quant_votos+=1
        selecionada.save()
    return HttpResponseRedirect(
        reverse('enquetes:resultados', args=(pergunta.id,))
        )
