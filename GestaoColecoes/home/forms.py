# -*- coding: utf-8 -*-
'''
Created on 23/05/2016

@author: Rafael Vict�ria-Pereira, 19960201
@author: Jo�o Machado, 20140014
'''

from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
