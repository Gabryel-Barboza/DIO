from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Choice, Question

# Create your views here.


# Views do MTV ou Controladores do MVC
# Orquestram as requisições da aplicação
# def index(request):
#     # Prática não recomendada, ineficiente e insegura
#     html = """\
#     <h1>Index</h1>
#     <p>You're at the index page of polls.</p>
# """
#     return HttpResponse(html)


# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')[:5]
#     response = '<br>'.join([q.question_text for q in latest_question_list])
#     return HttpResponse(response)


# Recuperando template para index
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    # Procura por um diretório de templates na pasta da aplicação polls
    template = loader.get_template('polls/index.html')
    # Mapeia os valores de variáveis descritas no template
    context = {'latest_question_list': latest_question_list}
    # Monta o arquivo HTML corretamente, substituindo variáveis por valores válidos
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exists')

    # render é uma shorthand para o processo de carregar templates acima
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # Shortcut para o tratamento de erro acima
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {'question': question, 'error_message': "You didn't select a choice."},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
