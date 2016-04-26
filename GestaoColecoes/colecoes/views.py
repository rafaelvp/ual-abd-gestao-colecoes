'''
Created on 24/03/2016

@author: Rafael Victoria-Pereira, 19960201
@author: Joao Machado, 20140014
'''

from django.http import HttpResponseRedirect
from django.shortcuts import render

from colecoes.forms import CollectionForm, CollectionItemForm
from colecoes.models import Collection, Collection_Item


# Create your views here.
def collection_detail(request, c_id):
    '''lists all the details of a collection '''
    collection = Collection.objects.filter(id = c_id).first()
    collections_detail = [collection.id, collection.name, collection.description, \
                          collection.type]
    context = {'collections_detail': collections_detail}
    return render(request, 'collection_detail.html', context)

def collection_delete(request, c_id):
    ''' deletes an existing collection '''
    # ToDo: create delete confirmation screen
    Collection.objects.filter(id = c_id).delete()
    return HttpResponseRedirect("/colecoes/")

def collection_update(request, c_id):
    ''' updates a collection'''
    if request.method == 'POST':
        form = CollectionForm(request.POST)
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
                         collection.type] for collection in Collection.objects.all()]
    context = {'collections_list' : collections_list}
    return render(request, 'collections_list.html', context)

# Collection_Item views
def collection_item_new(request, c_id):
    ''' creates a new collection '''
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
        except ValueError:
            print "Errors validating..."
    else:
        # If the request was not a POST, display the form to enter details.
        form = CollectionItemForm()
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        return render(request, 'collection_item_new.html', {'form': form})
    
def collection_item_list(request, c_id):
    ''' lists existing items of a given collection '''
    #Retrieve the selected collection
    selected_collection = Collection.objects.filter(id=c_id)
    #Query the database for items of that collection
    collection_items_list = [[collection_item.collection.id, collection_item.id, collection_item.item_series, \
                              collection_item.item_number, collection_item.description] \
                             for collection_item in Collection_Item.objects.filter(collection=selected_collection)]
    context = {'collection_items_list' : collection_items_list}
    return render(request, 'collection_items_list.html', context)