from django import forms

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