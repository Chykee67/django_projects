from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

@method_decorator(login_not_required, name="dispatch")
class HomePageView(TemplateView):
    template_name = 'eShop/home.html'