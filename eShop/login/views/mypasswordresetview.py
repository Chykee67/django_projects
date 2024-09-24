from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required
from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


from login.forms import ForgottenPasswordForm
from login.models import User


@method_decorator(login_not_required, name="dispatch")
class MyPasswordResetView(View):

    def get(self, request):
        return render(request, 'login/password_reset.html', {
            'form': ForgottenPasswordForm(),
        })
    
    def post(self, request):
        form = ForgottenPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            try:
                user = User.objects.get(email=email)
            except(KeyError, User.DoesNotExist):
                return render(request, 'login/password_reset.html', {
                    'form': ForgottenPasswordForm(),
                    'error_message': 'This email is not registered',
                })
            else:
                if form.confirm_password():
                    user.set_password(password1)
                    user.save()
                    return HttpResponseRedirect(reverse('login:login'))
                else:
                    return render(request, 'login/password_reset.html', {
                        'form': ForgottenPasswordForm(),
                        'error_message': 'Password Mismatch'
                    })
