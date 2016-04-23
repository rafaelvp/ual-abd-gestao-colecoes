'''
Created on 25/03/2016

@author: Rafael Victoria-Pereira, 19960201
'''

from django.conf.urls import patterns, url
from colecoes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
