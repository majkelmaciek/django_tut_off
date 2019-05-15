from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(
                request, 
                'alt_article_APP/index.html', 
                {'latest_question_list' : latest_question_list}
            )

def results(request, question_id):
    return HttpResponse("patrzysz na pytanie {}".format(question_id))

def detail(request, question_id):
    context = { 'question_MW' : get_object_or_404(Question, pk=question_id) }
    return render(request, 'alt_article_APP/detail.html', context)

def vote(request, question_id):
    return HttpResponse("udzielasz odpowiedzi na pytanie {}".format(question_id))

