'''
Created on 25/03/2016

@author: Rafael Victoria-Pereira, 19960201
'''

from django.conf.urls import patterns, url
from colecoes import views

urlpatterns = patterns('',
    url(r'^hello_world$', views.hello_world, name='hello_world'),
    url(r'^.*$', views.index, name='index'), #.* significa qualquer caracter, 0 ou mais vezes
    url(r'^fat_controller$', views.fat_controller, name='index_no_model'),
    url(r'^with_model$', views.model_controller, name='model_controller'),
    url(r'^MVC$', views.MVC_way, name='MVC_way'),
)
