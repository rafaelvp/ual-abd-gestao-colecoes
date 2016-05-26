# -*- coding: utf-8 -*-
'''
Created on 25/04/2016

@author: Rafael Victória-Pereira, 19960201
@author: João Machado, 20140014
'''

from django import forms
from django.contrib.auth.models import User
from django.http import request

from colecoes.models import Collection, Collection_Type, Collection_Item, User_Collection, User_Collection_Item


class CollectionTypeForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label = "Nome")
    # An inline class to provide additional information on the form.
    class Meta:
        model = Collection_Type
        fields = ['name']

class CollectionForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Collection_Type.objects.all(), to_field_name="id", label = "Tipo")
    name = forms.CharField(max_length=100, label = "Nome")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}), label = "Descrição")
    # An inline class to provide additional information on the form.
    class Meta:
        model = Collection
        fields = ['type', 'name', 'description']
        
class CollectionItemForm(forms.ModelForm):
    
    # additional code to disable the collection field
    def __init__(self, *args, **kwargs):
        super(CollectionItemForm, self).__init__(*args, **kwargs)
        self.fields['collection'].required = False
        self.fields['collection'].widget.attrs['disabled'] = 'disabled'
    
    # additional code to make sure the appropriate value is placed on field collection before the form is validated
    def clean_collection(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.collection
        else:
            return self.cleaned_data['collection']
            
    collection = forms.ModelChoiceField(queryset=Collection.objects.all(), to_field_name="id", label="Coleção")
    item_series = forms.CharField(max_length=10, label="Série", required=False)
    item_number = forms.IntegerField(label="Número")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 1}), label="Descrição")
    # An inline class to provide additional information on the form.
    class Meta:
        model = Collection_Item
        fields = ['collection', 'item_series', 'item_number', 'description']
        
class UserCollectionForm(forms.ModelForm):
    # The collection field  queryset here is just a placeholder, because it's overriden in views.py
    collection = forms.ModelChoiceField(queryset=Collection.objects.all(), to_field_name="id", label = "Coleção")

    # An inline class to provide additional information on the form.
    class Meta:
        model = User_Collection
        exclude = ('user',) # hide the user field on the form
        
class UserCollectionItemForm(forms.ModelForm):
    
    # The collection_item field  queryset here is just a placeholder, because it's overriden in views.py
    collection_item = forms.ModelChoiceField(queryset=Collection_Item.objects.all(), to_field_name="id", label="Item")
    # An inline class to provide additional information on the form.
    class Meta:
        model = User_Collection_Item
        fields = ['collection_item']
        exclude = ('user', 'user_collection',)