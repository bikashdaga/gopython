from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from django.http import HttpResponse
# from django.http import Http404
from django.template import loader

from .models import Question

def index(request): # display the lastest few question
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') # direct load from polls/templates/
    context = {
        'latest_question_list': lastest_question_list,
    } # context transfer to polls/index.html then show the index page in polls/
    # output = ', '.join([q.question_text for q in lastest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id): # displays a question text, without results but with a form to vote
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Sorry, Question does not exist!")
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)
    
def results(request, question_id): # displays results for a particular question
    response = "You are looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id): # handles voting for a particular choice in a particular question
    return HttpResponse("You're voting on questions %s." % question_id)