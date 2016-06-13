# -*- coding: utf-8 -*-
'''
Created on 23/05/2016

@author: Rafael Victória-Pereira, 19960201
@author: João Machado, 20140014
'''
from django import template 
from django.contrib.auth.models import Group 

from colecoes.models import Collection, Collection_Item, User_Collection_Item, \
    User_Collection, User_Message


# determinar se o user pertence a um grupo
# e disponibilizar via filtro para que possa ser usado nos templates
register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False


@register.filter(name='has_children') 
def has_children(object_id, object_type):
    if object_type == "Collection_Type":
        nbr_children = Collection.objects.filter(type = object_id).values('type').count()
        if nbr_children != 0:
            return True
        else:
            return False
    elif object_type == "Collection":
        nbr_children = Collection_Item.objects.filter(collection = object_id).values('collection').count()
        nbr_grandchildren = User_Collection.objects.filter(collection = object_id).values('collection').count()
        if ((nbr_children != 0) or (nbr_grandchildren != 0)):
            return True
        else:
            return False
    elif object_type == "Collection_Item":
        nbr_children = User_Collection_Item.objects.filter(collection_item = object_id).values('colection_item').count()
        if nbr_children != 0:
            return True
        else:
            return False
    elif object_type == "User_Collection":
        nbr_children = User_Collection_Item.objects.filter(user_collection = object_id).values('user_collection').count()
        if nbr_children != 0:
            return True
        else:
            return False
    elif object_type == "User_Collection_Item":
        user_collection_item = User_Collection_Item.objects.filter(id = object_id).first()
        nbr_children = Collection_Item.objects.filter(id = user_collection_item.collection_item).values('id').count()
        if nbr_children != 0:
            return True
        else:
            return False
        
@register.filter(name='has_new_messages')
def has_new_messages(user):
    unread_message_count = User_Message.objects.filter(receiver = user).filter(message_read = False).count()
    if unread_message_count != 0:
        return True
    else:
        return False
