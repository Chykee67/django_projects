from django import forms

class ProfilePhotoForm(forms.Form):
    photo = forms.ImageField()