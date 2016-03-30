'''
Created on 24/03/2016

@author: Rafael Victoria-Pereira, 19960201
'''
import cx_Oracle

from django.shortcuts import render
from django.http import HttpResponse
from colecoes.models import Collection

# Create your views here.
def hello_world(request):
    '''Basic Hello World inside the Controller - Without Model'''
    html = "<html><body>Hello Django World!</body></html>"
    return HttpResponse(html)

def fat_controller(request):
    '''Basic Hello World inside the Controller - Without Model'''

    #Conexao a base de dados
    connection = cx_Oracle.connect("gest_col/gcpassword@localhost:1521")

    #Pedido de dados a base de dados;
    cursor = connection.cursor()
    cursor.execute("select name from COLECOES_COLLECTION")
    rows = cursor.fetchall()
    if cursor.rowcount != 0:
        #rows = cursor.fetchall()
        html_ini = "<html><body></br><h1>Hello ABD...</h1></br>"
        for row in rows:
            if row[0] != 'FIFA 2016':
                html_ini = html_ini + "<p>" + str(row[0]) + "</p>"
            else:
                html_ini = html_ini + "<p style='color:red'>" + str(row[0]) + "</p>"
        html = html_ini + "</body></html>"
    else:
        html = "<html><body>Nada para mostrar!</body></html>"
        
    return HttpResponse(html)

def model_controller(request):
    '''Basic Hello World inside the Controller - Without Model'''
    #Neste caso a conexao a base de dados e feita pelo modelo;
    collections_list = [collectionObj.name for collectionObj in Collection.objects.all()]
    if collections_list:
        html_ini = "<html><body></br><h1>Hello ABD...I am getting data from the model</h1></br>"
        for row in collections_list:
            if row != 'FIFA 2016':
                html_ini = html_ini + "<p>" + row + "</p>"
            else:
                html_ini = html_ini + "<p style='color:red'>" + row + "</p>"
        html = html_ini + "</body></html>"
    else:
        html = "<html><body>Nada para mostrar ! </body></html>"
    return HttpResponse(html)

def MVC_way(request):
    '''O Controller (View no Django) deve ser fino! Quase sem codigo.
    Deve controlar e aplicar filtragens simples'''
    
    collection_list = [collection.name for collection in Collection.objects.all()]
    context = {'collection_list': collection_list}
    return render(request, 'collection.html', context)

def index(request):
    return HttpResponse("todas as outras paginas vem aqui parar...!")