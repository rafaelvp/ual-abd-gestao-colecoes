'''
Created on 25/04/2016

@author: Rafael Victoria-Pereira, 19960201
@author: Joao Machado, 20140014
'''

from django import forms
from colecoes.models import Collection, Collection_Type, Collection_Item

class CollectionForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    type = forms.ModelChoiceField(queryset=Collection_Type.objects.all(), to_field_name="id")
    # An inline class to provide additional information on the form.
    class Meta:
        model = Collection
        fields = ['name', 'description', 'type']
        
class CollectionItemForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        model = Collection_Item
        fields = ['collection', 'item_series', 'item_number', 'description']