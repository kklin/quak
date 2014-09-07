from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from quakapp import views

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', views.index, name='index'),
  url(r'', include('social_auth.urls')),
  url(r'^create/$', views.create, name='create'),
  url(r"^callback/$", views.callback, name="evernote_callback"),
  url(r'sorted_view/(?P<guid>[-\w]+)/$', views.sorted_view, name='sorted_view'),
  url(r'^presentation/(?P<guid>[-\w]+)/$', views.page, name='page'),
  url(r'^save/(?P<guid>[-\w]+)/$', views.auth, name='auth'),
  url(r"^auth/$", "auth", name="evernote_auth"),
  url(r'^incrementVote/$', views.increment_vote, name='increment_vote'),
  url(r'^newQuestion/$', views.new_question, name='new_question'))
