from django import forms
from django.contrib import admin

from .models import Floor, Section, Aisle, Item, Tag, Stock

admin.site.register(Floor)
admin.site.register(Section)
admin.site.register(Aisle)
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Stock)

# Register your models here.