from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

from store.models import Item

@method_decorator(login_not_required, name="dispatch")
class ItemView(DetailView):
    model = Item

    context_object_name = 'item'

    template_name = 'store/item.html'