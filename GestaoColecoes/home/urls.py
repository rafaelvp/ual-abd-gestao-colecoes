# -*- coding: utf-8 -*-
'''
Created on 23/05/2016

@author: Rafael Victória-Pereira, 19960201
@author: João Machado, 20140014
'''

from django.conf.urls import url, include
from home import views

urlpatterns = [
               url(r'^.*', views.index),
]
