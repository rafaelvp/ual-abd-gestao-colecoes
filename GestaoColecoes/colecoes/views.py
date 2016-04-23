'''
Created on 24/03/2016

@author: Rafael Victoria-Pereira, 19960201
'''
import cx_Oracle

from django.shortcuts import render
from django.http import HttpResponse
from colecoes.models import Collection

# Create your views here.
def index(request):
    return HttpResponse("todas as outras paginas vem aqui parar...!")