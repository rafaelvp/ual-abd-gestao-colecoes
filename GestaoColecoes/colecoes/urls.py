# -*- coding: utf-8 -*-
'''
Created on 25/03/2016

@author: Rafael Victória-Pereira, 19960201
@author: João Machado, 20140014
'''

from django.conf.urls import url
from colecoes import views

urlpatterns = [
   # collection urls
   url(r'^(?P<c_id>\d+)/?$', views.collection_detail),
   url(r'^(?P<c_id>\d+)/delete/?$', views.collection_delete),
   url(r'^(?P<c_id>\d+)/update/?$', views.collection_update),
   url(r'^new/?$', views.collection_new),
   
   # collection_item urls
   url(r'(\d+)/item/(\d+)/$', views.collection_item_detail),
   url(r'^(\d+)/item/(\d+)/delete/?$', views.collection_item_delete),
   url(r'^(\d+)/item/(\d+)/update/?$', views.collection_item_update),
   url(r'^(\d+)/item/new/?$', views.collection_item_new),
   url(r'^(?P<c_id>\d+)/item/.*?$', views.collection_item_list),
   
   # generic, catch-all url
   url(r'^.*$', views.collection_list),
]
