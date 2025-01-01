from django import forms


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
