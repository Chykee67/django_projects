from django import forms

from login.models import User


class Edit_ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "about_user",
        "country_of_residence", "state_of_residence", "city_of_residence", "street_address"
        ]