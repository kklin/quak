from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone
from Question import Question
from Presentation import Presentation
import Quak

def index(request):
  return HttpResponseRedirect('/quakapp/create/')

def create(request):
  context = RequestContext(request)
  if request.method == 'POST':
    title = request.POST['title']
    if not title:
      title = 'Untitled'
    guid = Quak.make_presentation(title)
    return HttpResponseRedirect('/quakapp/presentation/' + guid)
  else:
    pass
  return render_to_response('quakapp/create.html', {}, context)

def page(request, guid):
  context = RequestContext(request)
  context_dict = {}
  presentation = Quak.get_presentation(guid)
  context_dict['title'] = presentation.title
  context_dict['guid'] = presentation.guid
  context_dict['questions'] = []
  for question in presentation.questions:
    context_dict['questions'].append({
        'title': question.question
      , 'votes': question.votes
      , 'guid': question.guid
    })
  return render_to_response('quakapp/index.html', context_dict, context)

def increment_vote(request):
  context = RequestContext(request)
  guid = request.GET.get('guid', '')
  question = Quak.get_question_by_guid(guid)
  question.increment_vote_count()
  return HttpResponse('success')

def new_question(request):
  context = RequestContext(request)
  if request.method == 'POST':
    title = request.POST['question_title']
    guid = request.POST['presentation_guid']
    new_question = Quak.make_question(title, guid)
    return HttpResponseRedirect('/quakapp/presentation/' + guid)