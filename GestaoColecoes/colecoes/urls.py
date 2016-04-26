'''
Created on 25/03/2016

@author: Rafael Victoria-Pereira, 19960201
@author: Joao Machado, 20140014
'''

from django.conf.urls import patterns, url
from colecoes import views

urlpatterns = patterns('',
   # collection urls
   url(r'^(?P<c_id>\d+)/?$', views.collection_detail, name='collection_detail'),
   url(r'^(?P<c_id>\d+)/delete/?$', views.collection_delete, name='collection_delete'),
   url(r'^(?P<c_id>\d+)/update/?$', views.collection_update, name='collection_update'),
   url(r'^new/?$', views.collection_new, name='collection_new'),
   # collection_item urls
   #url(r'^(?P<c_id>\d+)/item/?P<i_id>d+/?$', views.collection_item_detail, name='collection_item_detail'),
   #url(r'^(?P<c_id>\d+)/item/?P<i_id>d+//delete/?$', views.collection_item_delete, name='collection_item_delete'),
   #url(r'^(?P<c_id>\d+)/item/?P<i_id>d+//update/?$', views.collection_item_update, name='collection_item_update'),
   #url(r'^(?P<c_id>\d+)/item/new/?$', views.collection_item_new, name='collection_item_new'),
   url(r'^(?P<c_id>\d+)/item/.*$', views.collection_item_list, name='collection_item_list'),
   # generic, catch-all url
    url(r'^.*$', views.collection_list, name='collection_list'),
)
