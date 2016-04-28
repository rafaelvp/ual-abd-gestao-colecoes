'''
Created on 27/04/2016

@author: Rafael Victoria-Pereira, 19960201
@author: Joao Machado, 20140014
'''

import os
os.environ["DJANGO_SETTINGS_MODULE"] = "GestaoColecoes.settings";

import django
django.setup()

from colecoes.models import Collection_Type, Collection, Collection_Item

print("module imported...")

def run():
    print("Podem existir registos nas tabelas - este script apaga todos os dados. \
    \n Tem a certeza que pretende continuar (y/n)?")
    choice = raw_input().lower()
    
    if choice == "n":
        return
    
    # Collection_Type section
    _collection_type = Collection_Type.objects.all()
    print _collection_type.count()
    
    if _collection_type.count() != 0:
        _collection_type.delete()
        
    Collection_Type.objects.bulk_create([
            Collection_Type(name = 'Cromos', id = 0),
            Collection_Type(name = 'Cartas Magic', id = 1)
    ])
    
    print("Collection_Type Done")
    
    # Collection section
    _collection = Collection.objects.all()
    
    if _collection.count() != 0:
        _collection.delete()
    Collection.objects.bulk_create([
            Collection(name = 'FIFA Euro 2016', description = 'Jogadores das equipas participantes no Euro 2016', type = Collection_Type.objects.filter(name = "Cromos")[0], id = 0),
            Collection(name = 'Invizimals', description = 'Cartas de batalha dos Invizimals', type = Collection_Type.objects.filter(name = "Cartas Magic")[0], id = 1),
            Collection(name = 'Animaizinhos', description = 'Fotos de animais fofinhos, da Panini', type = Collection_Type.objects.filter(name = "Cromos")[0], id = 2),
            Collection(name = 'Adrenalyn XL 1a Liga Portuguesa', description = 'Cartas de batalha da 1a liga 2015/16', type = Collection_Type.objects.filter(name = "Cartas Magic")[0], id = 3),
            Collection(name = 'O mundo de BATMAN', description = 'A Historia e as estorias do Cavaleiro Negro', type = Collection_Type.objects.filter(name = "Cromos")[0], id = 4),
    ])
    
    print("Collection Done")
    
        # Collection_Item section
    _collection_item = Collection_Item.objects.all()
    
    if _collection_item.count() != 0:
        _collection_item.delete()
        
    Collection_Item.objects.bulk_create([
            Collection_Item(collection = Collection.objects.filter(id = 0)[0], item_number = 1, description = 'Official Logo 1', id = 0),
            Collection_Item(collection = Collection.objects.filter(id = 0)[0], item_number = 2, description = 'Official Logo 2', id = 1),
            Collection_Item(collection = Collection.objects.filter(id = 0)[0], item_number = 3, description = 'Official Mascott', id = 2),
            Collection_Item(collection = Collection.objects.filter(id = 0)[0], item_number = 4, description = 'Panini sticker', id = 3),
            Collection_Item(collection = Collection.objects.filter(id = 0)[0], item_number = 5, description = 'Trophy 1', id = 4),
            Collection_Item(collection = Collection.objects.filter(id = 0)[0], item_number = 6, description = 'Trophy 2', id = 5),
            Collection_Item(collection = Collection.objects.filter(id = 0)[0], item_number = 7, description = 'UEFA Euro 2016 - Official Match Ball', id = 6),
            Collection_Item(collection = Collection.objects.filter(id = 1)[0], item_series = 'Elemental', item_number = 1, description = 'Elemental Fogo', id = 7),
            Collection_Item(collection = Collection.objects.filter(id = 1)[0], item_series = 'Elemental', item_number = 2, description = 'Elemental Gelo', id = 8),
            Collection_Item(collection = Collection.objects.filter(id = 1)[0], item_series = 'Elemental', item_number = 3, description = 'Elemental Deserto', id = 9),
            Collection_Item(collection = Collection.objects.filter(id = 1)[0], item_series = 'Elemental', item_number = 4, description = 'Elemental Selva', id = 10),
            Collection_Item(collection = Collection.objects.filter(id = 1)[0], item_series = 'Boxaroo', item_number = 1, description = 'Boxaroo Pup', id = 11),
            Collection_Item(collection = Collection.objects.filter(id = 1)[0], item_series = 'Boxaroo', item_number = 2, description = 'Boxaroo Colt', id = 12),
            Collection_Item(collection = Collection.objects.filter(id = 1)[0], item_series = 'Boxaroo', item_number = 3, description = 'Boxaroo Max', id = 13),
            Collection_Item(collection = Collection.objects.filter(id = 2)[0], item_series = 'G', item_number = 1, description = 'G01', id = 14),
            Collection_Item(collection = Collection.objects.filter(id = 2)[0], item_series = 'G', item_number = 2, description = 'G02', id = 15),
            Collection_Item(collection = Collection.objects.filter(id = 2)[0], item_series = 'G', item_number = 3, description = 'G03', id = 16),
            Collection_Item(collection = Collection.objects.filter(id = 2)[0], item_series = 'G', item_number = 4, description = 'G04', id = 17),
            Collection_Item(collection = Collection.objects.filter(id = 2)[0], item_series = 'Sticker', item_number = 1, description = 'Crazy Croc', id = 18),
            Collection_Item(collection = Collection.objects.filter(id = 2)[0], item_series = 'Sticker', item_number = 2, description = 'Happy Hippo', id = 19),
            Collection_Item(collection = Collection.objects.filter(id = 3)[0], item_series = 'Benfica', item_number = 1, description = 'Julio Cesar', id = 20),
            Collection_Item(collection = Collection.objects.filter(id = 3)[0], item_series = 'Benfica', item_number = 2, description = 'Jardel', id = 21),
            Collection_Item(collection = Collection.objects.filter(id = 3)[0], item_series = 'Benfica', item_number = 3, description = 'Luisao', id = 22),
            Collection_Item(collection = Collection.objects.filter(id = 4)[0], item_series = 'Heros', item_number = 1, description = 'Batman', id = 23),
            Collection_Item(collection = Collection.objects.filter(id = 4)[0], item_series = 'Heros', item_number = 2, description = 'Robin', id = 24),
            Collection_Item(collection = Collection.objects.filter(id = 4)[0], item_series = 'Heros', item_number = 3, description = 'Batgirl', id = 25),
            Collection_Item(collection = Collection.objects.filter(id = 4)[0], item_series = 'Vilains', item_number = 1, description = 'Joker', id = 26),
            Collection_Item(collection = Collection.objects.filter(id = 4)[0], item_series = 'Vilains', item_number = 2, description = 'Penguin', id = 27),
            Collection_Item(collection = Collection.objects.filter(id = 4)[0], item_series = 'Vilains', item_number = 3, description = 'Catwoman', id = 28),
    ])
    
    print("Collection_Item Done")
    
    print("All done!")
    
run();