from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from user_profile.models import Order


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