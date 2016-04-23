from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Collection_Type(models.Model):
    def __str__(self):
        return self.name
    
    collection_type_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, unique=True, db_index=True)
    status = models.BooleanField(default=True)
    status_datetime = models.DateTimeField()
    created_on = models.DateTimeField()
    created_by = models.CharField(max_length=50)

class Collection(models.Model):
    def __str__(self):
        return self.name
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.CharField(max_length=250)
    type = models.ForeignKey(Collection_Type, default=0, verbose_name = "the related collection type")
    status = models.BooleanField(default=True)
    status_datetime = models.DateTimeField()
    created_on = models.DateTimeField()
    created_by = models.CharField(max_length=50)
    
class Collection_Item(models.Model):
    def __str__(self):
        return self.item_series + str(self.item_number)
    
    id = models.AutoField(primary_key = True)
    collection_id = models.ForeignKey(Collection, default=0, verbose_name = "the related collection")
    item_series = models.CharField(max_length=10, null=True, blank=True)
    item_number = models.IntegerField()
    description = models.CharField(max_length=50)
    
class User_Collection(models.Model):
    def __str__(self):
        return self.collection.name
    
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, default=0, verbose_name = "the related collection owner")
    collection = models.ForeignKey(Collection, default=0, verbose_name = "the related collection")
    status = models.BooleanField(default=True)
    status_datetime = models.DateTimeField()
    created_on = models.DateTimeField()
    
class User_Collection_Item(models.Model):
    def __str__(self):
        return self.user_collection + '-' + self.collection_item
    
    id = models.AutoField(primary_key = True)
    user_collection = models.ForeignKey(User_Collection, default=0, verbose_name = "the related user collection")
    collection_item = models.ForeignKey(Collection_Item, default=0, verbose_name = "the related collection item")
    status = models.BooleanField(default=True)
    status_datetime = models.DateTimeField()
    created_on = models.DateTimeField()