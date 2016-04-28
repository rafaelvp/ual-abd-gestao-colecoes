# -*- coding: utf-8 -*-
'''
Created on 25/04/2016

@author: Rafael Victória-Pereira, 19960201
@author: João Machado, 20140014
'''

from django import forms
from colecoes.models import Collection, Collection_Type, Collection_Item

class CollectionForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label = "Nome")
    description = forms.CharField(max_length=250, label = "Descrição")
    type = forms.ModelChoiceField(queryset=Collection_Type.objects.all(), to_field_name="id", label = "Tipo")
    # An inline class to provide additional information on the form.
    class Meta:
        model = Collection
        fields = ['name', 'description', 'type']
        
class CollectionItemForm(forms.ModelForm):
    collection = forms.ModelChoiceField(queryset=Collection.objects.all(), to_field_name="id", label="Coleção")
    item_series = forms.CharField(max_length=10, label="Série")
    item_number = forms.IntegerField(label="Número")
    description = forms.CharField(max_length=50, label="Descrição")
    # An inline class to provide additional information on the form.
    class Meta:
        model = Collection_Item
        fields = ['collection', 'item_series', 'item_number', 'description']