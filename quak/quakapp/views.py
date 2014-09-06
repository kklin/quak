from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone

def index(request):
  context = RequestContext(request)
  return render_to_response('quakapp/index.html', {}, context)

def create(request):
  context = RequestContext(request)
  return render_to_response('quakapp/create.html', {}, context)

def page(request, notebook_id):
  context = RequestContext(request)
  return render_to_response('quakapp/page.html', {}, context)