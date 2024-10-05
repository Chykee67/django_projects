from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

from store.models import Section

@method_decorator(login_not_required, name="dispatch")
class SectionView(DetailView):
    model = Section
    template_name = 'store/storesectionview.html'
    context_object_name = 'section'