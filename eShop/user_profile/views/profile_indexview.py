from django.views import View
from django.shortcuts import render

class IndexView(View):

    def get(self, request):
        return render(request, 'user_profile/profile_indexview.html')

        