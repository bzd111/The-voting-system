# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question
# Create your views here.


def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    pass


def vote(request, question_id):
    pass
