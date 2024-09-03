from django import forms
from django.core import validators

class SignInForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        label_suffix='',
        max_length=100,
        )
    password = forms.CharField(
        label='Password',
        label_suffix='',
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput,
        )

class SignUpForm(forms.Form):
    user_name = forms.CharField(
        label='',
        label_suffix='',
        initial='User name',
        max_length=32,
    )

    user_email = forms.EmailField(
        label='',
        label_suffix='',
        initial='Email address',
        max_length=100,
    )

    password = forms.CharField(
        min_length=8,
        max_length=32,
        initial='Password',
        label='',
        label_suffix='',
        widget=forms.PasswordInput,
    )

    confirm_password = forms.CharField(
        initial='Confirm password',
        label='',
        label_suffix='',
    )

    about_user = forms.CharField(
        initial='Tell us about yourself',
        label='',
        label_suffix='',
        max_length='300',
        widget=forms.Textarea,
    )

    country_of_residence = forms.CharField(
        initial='Country of residence',
        label='',
        label_suffix='',
    )

    state_of_residence = forms.CharField(
        initial='State of residence',
        label='',
        label_suffix='',
    )

    city_of_residence = forms.CharField(
        initial='City of residence',
        label='',
        label_suffix='',
    )

    street_address = forms.CharField(
        initial = 'Street address',
        label='',
        label_suffix='',
        max_length=300,
        widget=forms.Textarea,
    )