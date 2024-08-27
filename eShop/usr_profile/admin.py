from django.contrib import admin

from .models import UserItem, Order, Notification

admin.site.register(UserItem)
admin.site.register(Order)
admin.site.register(Notification)

# Register your models here.
