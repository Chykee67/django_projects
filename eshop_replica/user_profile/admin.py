from django.contrib import admin

from .models import Cart, Order, Notification

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Notification)

# Register your models here.
