from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

from store.models import Section

@method_decorator(login_not_required, name="dispatch")
class HomePageView(TemplateView):
    template_name = 'eShop/homeview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = Section.sections.all()
        return context