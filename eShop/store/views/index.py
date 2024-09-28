from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator

from store.models import Section

@method_decorator(login_not_required, name="dispatch")
class IndexView(ListView):
    model = Section
    context_object_name = 'sections'
    template_name = 'store/index.html'