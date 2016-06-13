# -*- coding: utf-8 -*-
'''
Created on 25/03/2016

@author: Rafael Victória-Pereira, 19960201
@author: João Machado, 20140014
'''

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class Collection_Type(models.Model):
    def __str__(self):
        return self.name
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)

class Collection(models.Model):
    def __str__(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    type = models.ForeignKey(Collection_Type, default=0, verbose_name = "the related collection type")
    
class Collection_Item(models.Model):
    def __str__(self):
        return self.description
    
    def get_item_series_number(self):
        if self.item_series:
            return (self.item_series + "/" + str(self.item_number))
        else:
            return str(self.item_number)
    
    id = models.AutoField(primary_key = True)
    collection = models.ForeignKey(Collection, default=0, verbose_name = "the related collection")
    item_series = models.CharField(max_length=10, null=True, blank=True)
    item_number = models.IntegerField()
    description = models.CharField(max_length=50)
    
class User_Collection(models.Model):
    
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, default=0, verbose_name = "the related collection owner")
    collection = models.ForeignKey(Collection, default=0, verbose_name = "the related collection")
    
    def get_collection_name(self):
        return self.collection.name
    
class User_Collection_Item(models.Model):
    
    def get_item_series_number(self):
        if self.collection_item.item_series:
            return (self.collection_item.item_series + "/" + str(self.collection_item.item_number))
        else:
            return str(self.collection_item.item_number)
        
    def get_item_description(self):
        return self.collection_item.description
    
    id = models.AutoField(primary_key = True)
    user_collection = models.ForeignKey(User_Collection, default=0, verbose_name = "the related user collection")
    collection_item = models.ForeignKey(Collection_Item, default=0, verbose_name = "the related collection item")
    
class User_Message(models.Model):
    def mark_as_read(self):
        self.message_read = True
        self.message_read_date = datetime.now()
        self.save()
    
    id = models.AutoField(primary_key = True)
    sender = models.ForeignKey(User, default=0, related_name = "sender", verbose_name = "the message sender")
    receiver = models.ForeignKey(User, default=0, related_name = "receiver", verbose_name = "the message receiver")
    sent_date = models.DateTimeField()
    subject = models.CharField(max_length = 100)
    message = models.TextField()
    message_read = models.BooleanField(default=False)
    message_read_date = models.DateTimeField(null=True)
    
