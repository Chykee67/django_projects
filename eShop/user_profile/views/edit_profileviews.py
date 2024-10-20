from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from user_profile.forms import ProfilePhotoForm, Edit_ProfileForm

class UploadProfilePhotoView(View):
    def get(self, request):
        return render(request, 'user_profile/upload_profile_photo.html', {
            'form': ProfilePhotoForm(),
        })
    
    def post(self, request):
        form = ProfilePhotoForm(request.POST, request.FILES)

        if form.is_valid():
            request.user.profile_photo = request.FILES['photo']
            request.user.save()
            return HttpResponseRedirect(reverse('profile:index'))

class EditProfileDataView(View):
    def get(self, request):
        return render(request, 'user_profile/edit_profileview.html', {
            'form': Edit_ProfileForm(instance=request.user),
        })

    def post(self, request):
        ...