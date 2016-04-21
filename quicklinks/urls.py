try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import *
from quicklinks import views 

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quicklinks/$', views.links, name='links'),
    url(r'^index/$', views.indexAlt, name='index'),
]
