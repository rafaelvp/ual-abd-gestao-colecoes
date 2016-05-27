# -*- coding: utf-8 -*-
'''
Created on 24/03/2016

@author: Rafael Victoria-Pereira, 19960201
@author: João Machado, 20140014
'''

import cx_Oracle
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from GestaoColecoes.settings import DB_USER, DB_PASSWORD, DB_IP, DB_PORT
from colecoes.forms import CollectionTypeForm, CollectionForm, CollectionItemForm, \
                           UserCollectionForm, UserCollectionItemForm
from colecoes.models import Collection_Type, Collection, Collection_Item, \
                            User_Collection, User_Collection_Item
from colecoes.templatetags.app_filters import has_group, has_children


#from django.conf import settings
# Collection type views
def collection_type_new(request):
    ''' creates a new collection type'''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
    
    if request.method == 'POST':
        form = CollectionTypeForm(request.POST)
        try:
            # Have we been provided with a valid form?
            if form.is_valid():
                # Save the new category to the database.
                saved = form.save(commit=True)
                return HttpResponseRedirect("/colecoes/tipos/" + str(saved.pk) + "/")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
                return render(request, 'collection_type_new.html', {'form': form})
        except ValueError:
            print "Errors validating..."
    else:
        # If the request was not a POST, display the form to enter details.
        form = CollectionTypeForm()
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        return render(request, 'collection_type_new.html', {'form': form})

def collection_type_update(request, t_id):
    ''' updates a collection'''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
    
    if request.method == 'POST':
        # get the current "record" from the DB and pass it as instance
        # an extra step required in order to update the record
        # because by default Django will insert a new record
        collection_type_id = Collection_Type.objects.filter(id = t_id)
        instance = get_object_or_404(Collection_Type, id = collection_type_id)
        form = CollectionTypeForm(request.POST, instance = instance)
        try:
            if form.is_valid():
                # Save the new category to the database.
                saved = form.save(commit=True)
                return HttpResponseRedirect("/colecoes/tipos/" + str(saved.pk) + "/")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
                return render(request, 'collection_type_update.html', {'form': form, 'id':t_id})
        except ValueError:
            print "Errors validating..."
    else:
        collection_type = Collection_Type.objects.filter(id = t_id).first()
        form = CollectionTypeForm(instance=collection_type)
        return render(request, 'collection_type_update.html', {'form': form, 'id':t_id})

def collection_type_delete(request, t_id):
    ''' deletes an existing collection type'''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
    
    # Check for children in order to keep the database's referential integrity
    if has_children(t_id, "Collection_Type"):
        message1 = "Não é possível apagar este tipo de coleção porque existem coleções que o utilizam."
        message2 = "Apague essas coleções e tente novamente."
        context = {'message1': message1, 'message2': message2}
        return render(request, 'oops.html', context)
    else:
        Collection_Type.objects.filter(id = t_id).delete()
        return HttpResponseRedirect("/colecoes/tipos/")

def collection_type_detail(request, t_id):
    '''lists all the details of a collection type'''
    collection_type = Collection_Type.objects.filter(id = t_id).first()
    collection_types_detail = [collection_type.id, collection_type.name]
    context = {'collection_types_detail': collection_types_detail}
    return render(request, 'collection_type_detail.html', context)

def collection_type_list(request):
    ''' lists existing collection types '''
    # produce an alphabetically ordered by name list of collection types
    collection_types_list = [[collection_type.id, collection_type.name, \
                              Collection.objects.filter(type = collection_type).values('type').count()] \
                             for collection_type in Collection_Type.objects.all().order_by('name')]
    context = {'collection_types_list' : collection_types_list}
    return render(request, 'collection_types_list.html', context)

# Collection views
def collection_detail(request, c_id):
    '''lists all the details of a collection '''
    collection = Collection.objects.filter(id = c_id).first()
    collections_detail = [collection.id, collection.name, collection.description, \
                          collection.type]
    context = {'collections_detail': collections_detail}
    return render(request, 'collection_detail.html', context)

def collection_delete(request, c_id):
    ''' deletes an existing collection '''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
    
    # Check for children in order to keep the database's referential integrity
    if has_children(c_id, "Collection"):
        message1 = "Não é possível apagar esta coleção porque existem itens ou coleções de utilizador associados."
        message2 = "Apague os itens e/ou coleções de utilizador e tente novamente."
        context = {'message1': message1, 'message2': message2}
        return render(request, 'oops.html', context)
    else:
        Collection.objects.filter(id = c_id).delete()
        return HttpResponseRedirect("/colecoes/")

def collection_update(request, c_id):
    ''' updates a collection'''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
    
    if request.method == 'POST':
        # get the current "record" from the DB and pass it as instance
        # an extra step required in order to update the record
        # because by default Django will insert a new record
        collection_id = Collection.objects.filter(id = c_id)
        instance = get_object_or_404(Collection, id = collection_id)
        form = CollectionForm(request.POST, instance = instance)
        try:
            if form.is_valid():
                # Save the new category to the database.
                saved = form.save(commit=True)
                return HttpResponseRedirect("/colecoes/" + str(saved.pk) + "/")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
                return render(request, 'collection_update.html', {'form': form, 'id':c_id})
        except ValueError:
            print "Errors validating..."
    else:
        collection = Collection.objects.filter(id = c_id).first()
        form = CollectionForm(instance=collection)
        return render(request, 'collection_update.html', {'form': form, 'id':c_id})

def collection_new(request):
    ''' creates a new collection '''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
        
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        try:
            # Have we been provided with a valid form?
            if form.is_valid():
                # Save the new category to the database.
                saved = form.save(commit=True)
                return HttpResponseRedirect("/colecoes/" + str(saved.pk) + "/")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
                return render(request, 'collection_new.html', {'form': form})
        except ValueError:
            print "Errors validating..."
    else:
        # If the request was not a POST, display the form to enter details.
        form = CollectionForm()
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        return render(request, 'collection_new.html', {'form': form})

def collection_list(request):
    ''' lists existing collections
    if the user is logged in, shows a link to the user's collections '''
    collections_list = [[collection.id, collection.name, collection.description, \
                         collection.type, \
                         Collection_Item.objects.filter(collection = collection).count(), \
                         User_Collection.objects.filter(collection = collection).count(), \
                         ] for collection in Collection.objects.all().order_by('name')]
    context = {'collections_list' : collections_list}
    return render(request, 'collections_list.html', context)


# Collection_Item views
def collection_item_detail(request, c_id, i_id):
    '''lists all the details of a collection '''
    collection_item = Collection_Item.objects.filter(id = i_id).first()
    collection_id = collection_item.collection.id
    collection_name = collection_item.collection.name
    collection_items_detail = [collection_item.id, collection_id, collection_name, collection_item.item_series, \
                               collection_item.item_number, collection_item.description]
    context = {'collection_items_detail': collection_items_detail}
    return render(request, 'collection_item_detail.html', context)

def collection_item_new(request, c_id):
    ''' creates a new collection '''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
    
    if request.method == 'POST':
        form = CollectionItemForm(request.POST)
        try:
            # Have we been provided with a valid form?
            if form.is_valid():
                # Save the new category to the database.
                saved = form.save(commit=True)
                return HttpResponseRedirect("/colecoes/" + str(c_id) + '/item/' + str(saved.pk) + "/")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
                context = {'form': form, 'c_id': c_id}
                return render(request, 'collection_item_new.html', context)
        except ValueError:
            print "Errors validating..."
    else:
        # If the request was not a POST, display the form to enter details.
        # set the selected collection (passed in the c_id parameter) as the default value 
        # for the form's collection field 
        form = CollectionItemForm(initial={'collection': c_id})
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        context = {'form': form, 'c_id': c_id}
        return render(request, 'collection_item_new.html', context)

def collection_item_update(request, c_id, i_id):
    ''' updates a collection'''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
    
    if request.method == 'POST':
        # get the current "record" from the DB and pass it as instance
        # an extra step required in order to update the record
        # because by default Django will insert a new record
        collection_item_id = Collection_Item.objects.filter(id = i_id)
        instance = get_object_or_404(Collection_Item, id = collection_item_id)
        form = CollectionItemForm(request.POST, instance=instance)
        try:
            if form.is_valid():
                # Save the new category to the database.
                saved = form.save(commit=True)
                return HttpResponseRedirect("/colecoes/" + str(c_id) + "/item/" + str(saved.pk) + "/")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
                return render(request, 'collection_item_update.html', {'form': form, 'id':c_id, 'i_id':i_id})
        except ValueError:
            print "Errors validating..."
    else:
        collection_item = Collection_Item.objects.filter(id = i_id).first()
        form = CollectionItemForm(instance=collection_item)
        return render(request, 'collection_item_update.html', {'form': form, 'c_id':c_id, 'i_id':i_id} )

def collection_item_delete(request, c_id, i_id):
    ''' deletes an existing collection item'''
    # if the user is not a site admin, this function is not available
    if not (has_group(request.user, "site_admins")):
        raise PermissionDenied
    
    if has_children(c_id, "Collection_Item"):
        message1 = "Não é possível apagar este item porque está a ser usado em coleções de utilizador."
        message2 = "Apague os itens das coleções de utilizador e tente novamente."
        context = {'message1': message1, 'message2': message2}
        return render(request, 'oops.html', context)
    else:
        Collection_Item.objects.filter(id = i_id).delete()
        return HttpResponseRedirect("/colecoes/" + str(c_id) + '/item/' )
    
def collection_item_list(request, c_id):
    ''' lists existing items of a given collection '''
    #Retrieve the collection name
    c_name = Collection.objects.filter(id = c_id).first().name
    #Query the database for items of that collection
    collection_items_list = [[collection_item.id, \
                              collection_item.get_item_series_number(), \
                              collection_item.description] \
                             for collection_item in Collection_Item.objects.filter(collection = c_id)]
    context = {'collection_items_list' : collection_items_list, 'c_id':c_id, 'c_name':c_name}
    return render(request, 'collection_items_list.html', context)


# User_Collection views
def user_collection_list(request):
    ''' lists existing collections of the logged in user'''
    # prepare the context list with the following information:
    # IDs (user and collection)
    # Unique items of the collection registered by the user
    # Total items of the collection
    user_collections_list = [[user_collection.id, user_collection.collection, \
                              User_Collection_Item.objects.filter(user_collection = user_collection).values('collection_item__id').distinct().count(), \
                              Collection_Item.objects.filter(collection = user_collection.collection).count() \
                              ] \
                                 for user_collection in User_Collection.objects.filter(user=request.user).order_by('collection__name')]
    context = {'user_collections_list' : user_collections_list}
    return render(request, 'user_collections_list.html', context)

def user_collection_new(request):
    ''' creates a new user collection '''
    if request.method == 'POST':
        form = UserCollectionForm(request.POST)
        try:
            # Have we been provided with a valid form?
            if form.is_valid():
                # Save the new user collection to the database.
                saved = form.save(commit=False)
                # add the missing link to the user, which doesn't come from the form
                saved.user = request.user
                saved.save()
                return HttpResponseRedirect("/colecoes/user_col/" + str(saved.pk) + "/")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
                return render(request, 'user_collection_new.html', {'form': form})
        except ValueError:
            print "Errors validating..."
    else:
        
        # If the request was not a POST, display the form to enter details.
        form = UserCollectionForm()
        #override the available collections list, excluding the ones the user already has
        user_collections = User_Collection.objects.filter(user=request.user)
        user_collection_collection_ids = []
        for collection in user_collections:
            user_collection_collection_ids.append(collection.collection.id)
        form.fields['collection'].queryset=Collection.objects.all().exclude(id__in=user_collection_collection_ids).order_by('name')
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        return render(request, 'user_collection_new.html', {'form': form})
    
def user_collection_detail(request, c_id):
    '''lists all the details of a user collection '''
    user_collection = User_Collection.objects.filter(id = c_id).first()
    user_collection_detail = [user_collection.id, user_collection.collection]
    context = {'user_collection_detail': user_collection_detail}
    return render(request, 'user_collection_detail.html', context)

def user_collection_delete(request, c_id):
    ''' deletes an existing collection from the user's collection list'''
    # Check for children in order to keep the database's referential integrity
    if has_children(c_id, "User_Collection"):
        message1 = "Não é possível apagar esta coleção porque existem itens associados."
        message2 = "Apague os itens e tente novamente."
        context = {'message1': message1, 'message2': message2}
        return render(request, 'oops.html', context)
    else:
        User_Collection.objects.filter(id = c_id).delete()
        return HttpResponseRedirect("/colecoes/user_col/")

def user_collection_item_list(request, c_id):
    ''' lists existing items of a given user collection '''
    #Retrieve the collection name
    user_collection = User_Collection.objects.filter(id=c_id).first()
    c_name = user_collection.get_collection_name()
    # Find duplicate items in the user collection
    duplicate_items = find_item_duplicates(c_id)
    duplicate_items.fetchall()
    dup_count = duplicate_items.rowcount
    # Retrieve the collection item details for the list
    collection_items_list = [[item.id, item.get_item_series_number(), item.get_item_description()] \
                             for item in User_Collection_Item.objects.filter(user_collection = c_id).order_by('collection_item__item_series', 'collection_item__item_number')]
    # Prepare the context
    context = {'collection_items_list' : collection_items_list, 'c_id':c_id, 'c_name':c_name, 'dup_count':dup_count}
    return render(request, 'user_collection_items_list.html', context)

def user_collection_item_detail(request, c_id, i_id):
    '''lists all the items of a user's collection '''
    #Retrieve the collection from the user collection with the c_id
    user_collection = User_Collection.objects.filter(id=c_id).first()
    #Query the database for items of that collection
    # Retrieve the user collection item
    user_collection_item = User_Collection_Item.objects.filter(id = i_id).first()
    collection_items_detail = [i_id, c_id, user_collection.get_collection_name(), \
                               user_collection_item.get_item_series_number(), \
                               user_collection_item.get_item_description()]
    context = {'collection_items_detail': collection_items_detail}
    return render(request, 'user_collection_item_detail.html', context)

def user_collection_item_delete(request, c_id, i_id):
    ''' deletes an item from a user's collection'''
    # ToDo: create delete confirmation screen
    User_Collection_Item.objects.filter(id = i_id).delete()
    return HttpResponseRedirect("/colecoes/user_col/" + str(c_id) + '/item/' )

def user_collection_item_new(request, c_id):
    ''' adds a new collection item to a user's collection'''
    if request.method == 'POST':
        form = UserCollectionItemForm(request.POST)
        try:
            # Have we been provided with a valid form?
            if form.is_valid():
                # Save the new category to the database.
                saved = form.save(commit=False)
                user_collection = User_Collection.objects.filter(id = c_id).first()
                saved.user_collection = user_collection
                saved.save()
                return HttpResponseRedirect("/colecoes/user_col/" + str(c_id) + '/item/' + str(saved.pk) + "/")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
                context = {'form': form, 'c_id': c_id}
                return render(request, 'user_collection_item_new.html', context)
        except ValueError:
            print "Errors validating..."
    else:
        # If the request was not a POST, display the form to enter details.
        # restrict the collection items choice field to the items of the selected collection 
        form = UserCollectionItemForm()
        # Retrieve the user collection
        user_collection = User_Collection.objects.filter(id=c_id).first()
        # Then use it to get the collection_id
        collection = user_collection.collection
        # Finally, use the collection_id to restrict the collection_item choices to that collection
        # overriding the collection_item form field's choices (queryset)
        form.fields['collection_item'].queryset=Collection_Item.objects.filter(collection=collection)
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        context = {'form': form, 'c_id': c_id}
        return render(request, 'user_collection_item_new.html', context)

def user_collection_item_find_item_exchanges(request, c_id):
    ''' lists the possible exchanges for the duplicate items of a given user collection '''
    #Retrieve the collection name
    user_collection = User_Collection.objects.filter(id=c_id).first()
    c_name = user_collection.get_collection_name()
    collection_id = user_collection.collection.id
    # Find duplicate items in the user collection
    possible_exchanges_list = find_item_exchanges(c_id, collection_id)
    rows = possible_exchanges_list.fetchall()
    # Retrieve the collection item details for the list
    possible_exchanges_detail_list = []
    for row in rows:
        user = User.objects.filter(id = row[0]).first()
        collection_item = Collection_Item.objects.filter(id = row[2]).first()
        mailto = "mailto:" + user.email + "?subject=Troca%20de%20itens%20repetidos"
        possible_exchanges_detail_list.append([mailto, user.username, \
                                              collection_item.get_item_series_number(), collection_item])
    # Prepare the context
    context = {'possible_exchanges_detail_list' : possible_exchanges_detail_list, 'c_id':c_id, 'c_name':c_name}
    return render(request, 'user_collection_item_find_item_exchanges.html', context)
    
# Stored Procedure calls
def find_item_exchanges(user_collection_id, collection_id):  
    # create a cursor  
    connection_string = DB_USER + "/" + DB_PASSWORD + "@" + DB_IP + ":" + DB_PORT
    connection = cx_Oracle.connect(connection_string)
    cur = connection.cursor()
    out_cur = cur.var(cx_Oracle.CURSOR)
    out_query = cur.callproc("FIND_ITEM_EXCHANGES", (user_collection_id, collection_id, out_cur ))
    # grab the results in iterable form  
    results = out_query[2]
    #for row in results:
    #    print("user id = " + str(row[0]))
    #    print("user collection id = " + str(row[1]))
    #    print("collection item id = " + str(row[2])) 
    cur.close() 
    return results 

def find_item_duplicates(user_collection_id):  
    # create a cursor  
    connection_string = DB_USER + "/" + DB_PASSWORD + "@" + DB_IP + ":" + DB_PORT
    connection = cx_Oracle.connect(connection_string)
    cur = connection.cursor()
    out_cur = cur.var(cx_Oracle.CURSOR)
    out_query = cur.callproc("FIND_ITEM_DUPLICATES", (user_collection_id, out_cur ))
    # grab the results in iterable form  
    results = out_query[1]
    #for row in results:
    #    print("user id = " + str(row[0]))
    #    print("user collection id = " + str(row[1]))
    #    print("collection item id = " + str(row[2])) 
    cur.close() 
    return results