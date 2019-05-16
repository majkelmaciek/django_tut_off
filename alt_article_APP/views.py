from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
from django.db.models import F

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(
                request, 
                'alt_article_APP/index.html', 
                {'latest_question_list' : latest_question_list},
            )

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'alt_article_APP/results.html', {'question' : question})

def detail(request, question_id):
    context = { 'question_MW' : get_object_or_404(Question, pk=question_id) }
    return render(request, 'alt_article_APP/detail.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.filter(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, "alt_article_APP/detail.html", {
            'question_MW': question,
            'errorMessage': "Nie wybrales żadnej odpowiedzi.",
        })
    else:
        # update() with F() is doing work that blocks occuring hazard (race condition)
        selected_choice.update( votes = F('votes')+1 )
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('alt_article_APP:results', args=(question.id,)))