from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone
from Question import Question
from Presentation import Presentation
import Quak

last_guid = ""

EN_CONSUMER_KEY = 'kklin'
EN_CONSUMER_SECRET = '78932d6049811172'

def get_evernote_client(token=None):
    if token:
        return EvernoteClient(token=token, sandbox=True)
    else:
        return EvernoteClient(
            consumer_key=EN_CONSUMER_KEY,
            consumer_secret=EN_CONSUMER_SECRET,
            sandbox=True
        )

def index(request):
  return HttpResponseRedirect('/create/')

def auth(request, guid):
  last_guid = guid
  client = get_evernote_client()
  callbackUrl = 'http://%s%s' % (
      request.get_host(), reverse('evernote_callback'))
  request_token = client.get_request_token(callbackUrl)

  # Save the request token information for later
  request.session['oauth_token'] = request_token['oauth_token']
  request.session['oauth_token_secret'] = request_token['oauth_token_secret']

  # Redirect the user to the Evernote authorization URL
  return redirect(client.get_authorize_url(request_token))

def callback(request):
  access_token = ""
  try:
      client = get_evernote_client()
      access_token = client.get_access_token(
          request.session['oauth_token'],
          request.session['oauth_token_secret'],
          request.GET.get('oauth_verifier', '')
      )
      Quak.gen_student_evernote(last_guid, access_token)
  except KeyError:
      return redirect('/')

  return HttpResponse('done')

def create(request):
  context = RequestContext(request)
  if request.method == 'POST':
    title = request.POST['title']
    if not title:
      title = 'Untitled'
    guid = Quak.make_presentation(title)
    if guid:
        return HttpResponseRedirect('/presentation/' + guid)
    else:
        return HttpResponseRedirect('/create/')
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

def save(request, guid):
  context = RequestContext(request)
  context_dict = {}
  presentation = Quak.get_presentation(guid)
  context_dict['title'] = presentation.title
  context_dict['guid'] = presentation.guid
  if request.method == 'POST':
    pass
  else:
    return render_to_response('quakapp/save.html', context_dict, context)

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
    return HttpResponseRedirect('/presentation/' + guid)