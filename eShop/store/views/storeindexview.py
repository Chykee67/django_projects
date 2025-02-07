from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.contrib.auth.models import Group

from store.models import Section, Tag

@method_decorator(login_required, name="dispatch")
class IndexView(View):

    template_name = 'store/storeindexview.html'

    def get(self, request):
        adults = Group.objects.get(name='adults')
        if adults in request.user.groups.all():
            adult_perms = 1
        else:
            adult_perms = 0

        return render(request, self.template_name, {
            'sections': Section.sections.all(),
            'adult_perms': adult_perms,
            'adult_tag': Tag.tags.get(description='adults'),
        })