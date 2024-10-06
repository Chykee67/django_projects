from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from  django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from user_profile.models import Order
from store.models import Item


class OrdersTemplateView(TemplateView):
    template_name = 'user_profile/profile_orders_indexview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_orders'] = Order.orders.filter(user=self.request.user)
        return context

class OrdersListView(ListView):
    ...

class OrderDetailView(DetailView):
    ...#Stopped at 416

class CreateOrderView(View):
    def get(self, request):
        return render(request, 'user_profile/profile_create_orderview.html')

    def post(self, request):
        ...

class ConfirmOrderView(View):
    
    def get(self, request, item_description):
        item = Item.items.get(description=item_description)
        return render(request, 'user_profile/profile_confirm_orderview.html', {
            "item": item,
        })

    def post(self, request, item_description):

        item = request.user.cart.items.get(description=item_description)

        unit, unit_price = request.POST['purchase_details'].split(',')

        quantity = request.POST['quantity']

        Order.orders.create(
            user=request.user,
            item=item,
            unit=unit,
            quantity=quantity,
            per_unit_charge=unit_price,
        )

        request.user.cart.items.remove(item)

        return HttpResponseRedirect(reverse('profile:orders'))