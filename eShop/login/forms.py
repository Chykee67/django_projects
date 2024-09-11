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

    email = forms.EmailField(
        label='Email',
        label_suffix='',
        max_length=100,
    )

    password1 = forms.CharField(
        min_length=8,
        max_length=32,
        label='Password',
        label_suffix='',
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label='Confirm password',
        label_suffix='',
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput,
    )

    date_of_birth = forms.DateField()

    first_name = forms.CharField(
        label="First name",
        label_suffix="",
        max_length=40,
    )

    last_name = forms.CharField(
        label="Last name",
        label_suffix="",
        max_length=40,
    )

    def confirm_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            return False
        else:
            return True


class ForgottenPasswordForm(forms.Form):
    email = forms.EmailField(
        label = 'Email',
        label_suffix = '',
        max_length = 100,
    )

    password1 = forms.CharField(
        min_length=8,
        max_length=32,
        label='Password',
        label_suffix='',
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label='Confirm password',
        label_suffix='',
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput,
    )

    def confirm_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            return False
        else:
            return True


class EditUserProfileForm(forms.Form):
    """
    Form for editing user regisration data
    """
    first_name = forms.CharField(
        label='First name',
        label_suffix='',
        max_length=40,
        required=False,
    )

    last_name = forms.CharField(
        label='Last name',
        label_suffix='',
        max_length=40,
        required=False,
    )

    date_of_birth = forms.DateField(
        label_suffix='',
        initial='1970-01-01',
        required=False,
    )

    about_user = forms.CharField(
        label='About you',
        label_suffix='',
        widget=forms.Textarea,
        max_length=300,
        required=False,
    )

    country_of_residence = forms.CharField(
        label='Country of Residence',
        label_suffix='',
        max_length=100,
        required=False,
    )

    state_of_residence = forms.CharField(
        label='State of Residence',
        label_suffix='',
        max_length=100,
        required=False,
    )

    city_of_residence = forms.CharField(
        label='City of Residence',
        label_suffix='',
        max_length=100,
        required=False,
    )

    street_address = forms.CharField(
        label='Street Address',
        label_suffix='',
        max_length=300,
        widget=forms.Textarea,
        required=False,
    )