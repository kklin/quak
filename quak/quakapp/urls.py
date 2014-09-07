from django.conf.urls import patterns, url
from quakapp import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'presentation/(?P<guid>[-\w]+)/$', views.page, name='page'),
  url(r'sorted_view/(?P<guid>[-\w]+)/$', views.sorted_view, name='sorted_view'),
  url(r'incrementVote/$', views.increment_vote, name='increment_vote'),
  url(r'newQuestion/$', views.new_question, name='new_question'))
