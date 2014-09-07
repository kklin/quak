from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone

def index(request):
  context = RequestContext(request)
  return render_to_response('quakapp/index.html', {}, context)

def create(request):
  context = RequestContext(request)
  if request.method == 'POST':
    title = request.POST['title']
    if not title:
      title = 'Untitled'
    guid = 123
    return HttpResponseRedirect('/quakapp/page/' + guid)
  else:
    pass
  return render_to_response('quakapp/create.html', {}, context)

def page(request, notebook_id):
  context = RequestContext(request)
  context_dict = {}
  context_dict['title'] = "CS61C Lecture 4"
  context_dict['questions'] = [{
      'title': 'What is the best way to eat pizza??'
    , 'votes': 10
    , 'time': 123
    , 'guid': 1
  }, {
      'title': 'Why is Sahil Patel so cool??!'
    , 'votes': 200
    , 'time': 1234
    , 'guid': 1
  }, {
      'title': 'Why is Sahil Patel so cool??!'
    , 'votes': 200
    , 'time': 1232
    , 'guid': 1
  }]
  return render_to_response('quakapp/page.html', context_dict, context)

def increment_vote(request):
  context = RequestContext(request)
  guid = request.GET.get('guid', '')
  question = get_question(guid)
  if question:
    question = get_question(guid)
    return HttpResponse('success')
  else:
    return HttpResponse('error')

def new_question(request):
  return False


def get_question(guid):
  return False