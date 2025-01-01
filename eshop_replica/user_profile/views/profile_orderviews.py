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

class OrdersListView(View):

    def get(self, request, orders_list):
        if orders_list == 'pending':
            orders = request.user.order_set.pending()
        elif orders_list == 'paid_for':
            orders = request.user.order_set.paid_for()
        elif orders_list == 'delivered':
            orders = request.user.order_set.delivered()
        else:
            orders = 'invalid order query'
        
        return render(request, 'user_profile/profile_orders_listview.html', {
            'orders': orders,
            'orders_list': orders_list,
        })

class OrderDetailView(View):
    def get(self, request, order_id):
        return render(request, 'user_profile/profile_order_detailsview.html', {
            'order': request.user.order_set.get(id=order_id),
        })

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