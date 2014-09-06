from django.conf.urls import patterns, url
from quakapp import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'page/(?P<notebook_id>\w+)/$', views.page, name='page'))