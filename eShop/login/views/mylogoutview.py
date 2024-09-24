from django.views import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login:login'))