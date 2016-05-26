from django.contrib import admin
from colecoes.models import Collection, Collection_Item, Collection_Type, User_Collection, User_Collection_Item

# Register your models here.
admin.site.register(Collection_Type)
admin.site.register(Collection)
admin.site.register(Collection_Item)
admin.site.register(User_Collection)
admin.site.register(User_Collection_Item)