from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

from store.models import Section

@method_decorator(login_not_required, name="dispatch")
class TrendingView(ListView):
    model = Section

    context_object_name = 'trends'

    template_name = 'store/trending.html'

    def get_queryset(self):
        return Section.sections.order_by("description")[:2]