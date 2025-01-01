from django import forms


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
