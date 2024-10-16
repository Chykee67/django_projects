from django import forms

class ProfilePhotoForm(forms.Form):
    title = forms.CharField(
        max_length=100,
    )
    photo = forms.ImageField()