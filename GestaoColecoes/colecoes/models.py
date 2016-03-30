from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Collection(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    status_datetime = models.DateTimeField()
    created_on = models.DateTimeField()
    created_by = models.CharField(max_length=50)
    
class CollectionItem(models.Model):
    id = models.AutoField(primary_key = True)
    collection_id = models.ForeignKey(Collection, verbose_name = "the related collection")
    item_series = models.CharField(max_length=10, null=True, blank=True)
    item_number = models.IntegerField()
    description = models.CharField(max_length=50)
