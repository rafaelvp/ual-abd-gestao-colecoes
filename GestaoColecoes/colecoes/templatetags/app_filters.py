# -*- coding: utf-8 -*-
'''
Created on 23/05/2016

@author: Rafael Victória-Pereira, 19960201
@author: João Machado, 20140014
'''
from django import template 
from django.contrib.auth.models import Group 

# determinar se o user pertence a um grupo
# e disponibilizar via filtro para que possa ser usado nos templates
register = template.Library() 
@register.filter(name='has_group') 

def has_group(user, group_name):
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False
