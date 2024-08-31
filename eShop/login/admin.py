from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User


class UserCreationForm(forms.ModelForm):

    """
    Form for creating a user. Contains all required fields and a repeated password
    """

    password1 = forms.CharField(
        label = "password",
        widget = forms.PasswordInput,
    )

    password2 = forms.CharField(
        label = "password confirmation",
        widget = forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "country_of_residence",
            "state_of_residence",
            "city_of_residence",
            "street_address",
            "email",
        ]

    def clean_password2(self):

        #Check that password1 and password2 are the same

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):

        #Save the provided passowrd in hashed format

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """
    For updating user data. Includes all user data fields, password is replaced by admin disabled hashed password
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "country_of_residence",
            "state_of_residence",
            "city_of_residence",
            "street_address",
            "email",
            "about_user",
            "is_active",
            "is_admin",
        ]

class UserAdmin(BaseUserAdmin):
    """
    Forms to add and change user instances
    """

    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    list_display = [
            "first_name",
            "last_name",
            "date_of_birth",
            "country_of_residence",
            "state_of_residence",
            "city_of_residence",
            "street_address",
            "email",
            "about_user",
            "is_active",
            "is_admin",
        ]
        
    list_filter = ["is_admin"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": [
            "first_name",
            "last_name",
            "date_of_birth",
            "country_of_residence",
            "state_of_residence",
            "city_of_residence",
            "street_address",
            "about_user",
        ]}),
        ("Permissions", {"fields": ["is_admin"]})
    ]

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
            "first_name",
            "last_name",
            "date_of_birth",
            "country_of_residence",
            "state_of_residence",
            "city_of_residence",
            "street_address",
            "email",
            "password1",
            "password2"
        ]
            }
        )
    ]

    search_fields = ["email"] #["first_name, "lasr_name"]
    ordering = ["email"]
    filter_horizontal = []

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
