from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from quakapp import views

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'sorted_view/(?P<guid>[-\w]+)/$', views.sorted_view, name='sorted_view'),
  url(r'^presentation/(?P<guid>[-\w]+)/$', views.page, name='page'),
  url(r'^incrementVote/$', views.increment_vote, name='increment_vote'),
  url(r'^newQuestion/$', views.new_question, name='new_question'))
