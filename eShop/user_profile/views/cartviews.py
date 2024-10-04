from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

class CartView(ListView):
    template_name = 'user_profile/cartview.html'
    context_object_name = 'mycart_items'

    def get_queryset(self):
        mycart = self.request.user.cart
        return mycart.items.all()

class RemoveItemView(View):
    def get(self, request, item_description):
        mycart = request.user.cart
        mycart.items.get(description=item_description).delete()
        return HttpResponseRedirect(reverse('profile:cart'))

