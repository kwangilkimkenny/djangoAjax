import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Ajax 적용부분
from django.http import JsonResponse
from django.template import RequestContext
from django.template import loader

from ai.math_gen.mathGen import math_qeus_gen

# Create your views here.
def index(request):
    print("Clicked home")
    main = math_qeus_gen()
    pre_question = main.make_question()
    dataset = {
        "pre_question" : pre_question,
    }
    return render(request, 'ai/index.html', dataset)


def goto_index(request):
    return render(request, 'index.html', {})


def test(request):
    return render(request, 'ai/test.html', {})


def createData(request):
    main = math_qeus_gen()
    if request.method == 'POST':
        answer_re = request.POST['answer']
        print("createData : ", answer_re)
        ques_ans = main.startTest(answer_re)
        answer_re = ques_ans["result"]
        re_time = ques_ans["result_time"]

        return HttpResponse(answer_re, re_time)

