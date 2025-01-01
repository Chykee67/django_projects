from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

from store.models import Item

@method_decorator(login_not_required, name="dispatch")
class ItemView(View):

    def get(self, request, item_description):
        if request.session.get('add_to_cart_error', False):
            error = request.session['add_to_cart_error']
            del request.session['add_to_cart_error']
        else:
            error = False
        return render(request, 'store/storeitemview.html', {
            'item': get_object_or_404(Item, description=item_description),
            'add_to_cart_error': error,
        })


class AddToCartView(View):

    def get(self, request, item_description):
        item = get_object_or_404(Item, description=item_description)
        mycart = request.user.cart
        if item in mycart.items.all():
            request.session['add_to_cart_error'] = 'Already added to cart. Please edit quantity at checkout'
            return HttpResponseRedirect(reverse('store:item', args=(item_description,)))
        else:
            mycart.items.add(item)
            return HttpResponseRedirect(reverse('store:item', args=(item_description,)))