from multiprocessing import context
from re import template
import copy
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Fields, Generation
from .forms import Answer1, ContactForm

ques = []
question_number = 0
sum_number = 0
correct_answer = [] # 1：正解　0：不正解
q_answer = []
PRODUCTION_NUMBER = 20

def home(request):
    template = loader.get_template('law_app/index.html')
    context = {'fname':'成功！'}
    return HttpResponse(template.render(context, request))

def practice(request):
    generation = Generation.objects.all()
    fields = Fields.objects.all()
    template = loader.get_template('law_app/practice.html')
    check = 0
    if request.method == "POST":
        check = request.POST.get("ques_sum_number")
        print(check)
    context = {
        "generation" : generation,
        "fields" : fields,
        "check" : check
        }
    
    return HttpResponse(template.render(context, request))

def practice_main(request):
    global ques, question_number, q_answer, correct_answer, sum_number
    ques = []
    q_answer = []
    correct_answer = []
    question_number = 0
    template = loader.get_template('law_app/practice_main.html')
    input_fields = []
    sum_number = 0
    if request.method == "POST":
        ques2 = []
        input_fields = request.POST.getlist("all_field")
        input_generation = request.POST.getlist("all_generation")
        sum_number = int(request.POST.get("ques_sum_number"))
        for gen in input_generation:
            ques += Question.objects.filter(generation=gen, q_format_id=1)
        for fie in input_fields:
            ques2 += Question.objects.filter(fields=fie, q_format_id=1)
        ques1 = copy.deepcopy(ques2)
        for i in ques:
            for j in ques1:
                if i == j:
                    ques2.remove(j)
        ques += ques2
    random.shuffle(ques)
    context = {
            'question' : ques[question_number],
            'number' : question_number
    }
    return HttpResponse(template.render(context, request))

def practice_question(request, slug):
    global question_number
    template = loader.get_template('law_app/practice_question.html')
    question = Question.objects.get(slug=slug)
    count = 0
    for q in ques:
        if q == question:
            break
        count += 1
    question_number = count
    ans_form = Answer1()
    context = {
        'number' : question_number+1,
        'question':question,
        'before' : ques[question_number-1],
        'ans_form': ans_form
    }
    return HttpResponse(template.render(context, request))

def practice_answer(request):
    global q_answer, correct_answer, question_number
    template = loader.get_template('law_app/practice_answer.html')
    now_number = question_number
    question_number += 1
    end = 0
    form = Answer1(request.POST)
    if form.is_valid():
        answer_temporary = form.cleaned_data['answer']
        answer_main = ""
        for ans in answer_temporary:
            answer_main += ans
        if len(q_answer) > now_number+1:
            q_answer[now_number] = answer_main
        else: q_answer.append(answer_main)
        if q_answer[now_number] == ques[now_number].answer:
            if len(q_answer) > now_number+1:
                correct_answer[now_number] = 1
            else: correct_answer.append(int(1))
        else:
            if len(q_answer) > now_number+1:
                correct_answer[now_number] = 0
            else: correct_answer.append(int(0))
    
    if now_number == sum_number-1:
        end = 1
    print(end)
    context = {
        'number' : question_number,
        'sum_number' : sum_number,
        'question' : ques[now_number],
        'answer' : q_answer[now_number],
        'correct' : correct_answer[now_number],
        'next' : ques[question_number],
        'before' : ques[now_number-1],
        'end' : end
    }
    return HttpResponse(template.render(context, request))

def practice_end(request):
    global  correct_answer
    template = loader.get_template('law_app/practice_end.html')
    del correct_answer[sum_number:]
    context = {
        'question' : ques,
        'result' : correct_answer,
        'answer' : q_answer
    }
    return HttpResponse(template.render(context, request))

def production_start(request):
    template = loader.get_template('law_app/production_start.html')
    context = {'i' : 'okemaru'}
    return HttpResponse(template.render(context, request))

def production(request):
    global ques
    template = loader.get_template('law_app/production.html')
    ques = []
    ques += Question.objects.all()
    random.shuffle(ques)
    number = [i for i in range(PRODUCTION_NUMBER)]
    context = {
        'number' : number,
        'question' : ques,
    }
    return HttpResponse(template.render(context, request))

def production_answer(request):
    template = loader.get_template('law_app/production_answer.html')
    number = [i for i in range(PRODUCTION_NUMBER)]
    context = {
        'number' : number,
        'question' : ques
    }
    return HttpResponse(template.render(context, request))

def create_pdf(request):
    template = loader.get_template('law_app/create_pdf.html')
    context = {
        'i' : 'okemaru'
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('law_app/contact.html')
    contact_form = ContactForm()
    sending = 0
    if request.method == "POST":
        sending = 1
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
    context = {
        'form' : contact_form,
        'send' : sending
    }
    return HttpResponse(template.render(context, request))
