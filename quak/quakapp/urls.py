from django.conf.urls import patterns, url
from quakapp import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'page/(?P<notebook_id>\w+)/$', views.page, name='page'),
  url(r'incrementVote/$', views.increment_vote, name='increment_vote'),
  url(r'newQuestion/$', views.new_question, name='new_question'))