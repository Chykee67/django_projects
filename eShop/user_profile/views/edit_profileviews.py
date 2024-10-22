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
        else:
            return HttpResponse(form.errors)

class EditProfileDataView(View):
    def get(self, request):
        return render(request, 'user_profile/edit_profileview.html', {
            'form': Edit_ProfileForm(instance=request.user),
        })

    def post(self, request):
        form = Edit_ProfileForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['first_name'] != '' and form.cleaned_data['first_name'] != request.user.first_name:
                request.user.first_name = form.cleaned_data['first_name']
            else: pass
            if form.cleaned_data['last_name'] != '' and form.cleaned_data['last_name'] != request.user.last_name:
                request.user.last_name = form.cleaned_data['last_name']
            else: pass
            if form.cleaned_data['about_user'] != '' and form.cleaned_data['about_user'] != request.user.about_user:
                request.user.about_user = form.cleaned_data['about_user']
            else: pass
            if form.cleaned_data['country_of_residence'] != '' and form.cleaned_data['country_of_residence'] != request.user.country_of_residence:
                request.user.country_of_residence = form.cleaned_data['country_of_residence']
            else: pass
            if form.cleaned_data['state_of_residence'] != '' and form.cleaned_data['state_of_residence'] != request.user.state_of_residence:
                request.user.state_of_residence = form.cleaned_data['state_of_residence']
            else: pass
            if form.cleaned_data['city_of_residence'] != '' and form.cleaned_data['city_of_residence'] != request.user.city_of_residence:
                request.user.city_of_residence = form.cleaned_data['city_of_residence']
            else: pass
            if form.cleaned_data['street_address'] != '' and form.cleaned_data != request.user.street_address:
                request.user.street_address = form.cleaned_data['street_address']
            else: pass

            request.user.save()

            return HttpResponseRedirect(reverse('profile:index'))
        else:
            return HttpResponse(form.errors)
