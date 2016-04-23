from django.contrib import admin
from colecoes.models import Collection, Collection_Item, Collection_Type

# Register your models here.
admin.site.register(Collection_Type)
admin.site.register(Collection)
admin.site.register(Collection_Item)
