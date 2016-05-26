# -*- coding: utf-8 -*-
'''
Created on 25/03/2016

@author: Rafael Victória-Pereira, 19960201
@author: João Machado, 20140014
'''

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from colecoes import views

urlpatterns = [
    # Admin
    #url(r'^admin/', include(admin.site.urls)),
    
   # collection type urls
   url(r'^tipos/(?P<t_id>\d+)/delete/?$', views.collection_type_delete),
   url(r'^tipos/(?P<t_id>\d+)/update/?$', views.collection_type_update),
   url(r'^tipos/(?P<t_id>\d+)/?$', views.collection_type_detail),
   url(r'^tipos/new/?$', views.collection_type_new),
   url(r'^tipos/*$', views.collection_type_list),
   
   # user_collection_item urls
   url(r'user_col/(\d+)/item/(\d+)/$', login_required(views.user_collection_item_detail)),
   url(r'^user_col/(\d+)/item/(\d+)/delete/?$', login_required(views.user_collection_item_delete)),
   url(r'^user_col/(\d+)/item/new/?$', login_required(views.user_collection_item_new)),
   url(r'^user_col/(\d+)/item/?$', login_required(views.user_collection_item_list)),
   
   # user_collection urls
   url(r'^user_col/(\d+)/?$', login_required(views.user_collection_detail)),
   url(r'^user_col/(\d+)/delete/?$', login_required(views.user_collection_delete)),
   url(r'^user_col/new/?$', login_required(views.user_collection_new)),
   url(r'^user_col/', login_required(views.user_collection_list)),
   
   # collection urls
   url(r'^(?P<c_id>\d+)/?$', views.collection_detail),
   url(r'^(?P<c_id>\d+)/delete/?$', views.collection_delete),
   url(r'^(?P<c_id>\d+)/update/?$', views.collection_update),
   url(r'^new/?$', views.collection_new),
   
   # collection_item urls
   url(r'(\d+)/item/(\d+)/?$', views.collection_item_detail),
   url(r'^(\d+)/item/(\d+)/delete/?$', views.collection_item_delete),
   url(r'^(\d+)/item/(\d+)/update/?$', views.collection_item_update),
   url(r'^(\d+)/item/new/?$', views.collection_item_new),
   url(r'^(\d+)/item/?$', views.collection_item_list),
   
   # generic, catch-all url
    url(r'^.*$', views.collection_list),
]
