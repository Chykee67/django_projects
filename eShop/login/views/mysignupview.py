from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect


from login.forms import SignUpForm
from login.models import User



@method_decorator(login_not_required, name="dispatch")
class MySignupView(View):
    def get(self, request):
        return render(request, 'login/mysignupview.html', {
            'form': SignUpForm(),
        })

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
            except (KeyError, User.DoesNotExist):
                if form.confirm_password():
                    new_user = User.objects.create_user(
                        email=form.cleaned_data['email'],
                        date_of_birth=form.cleaned_data['date_of_birth'],
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        password=form.cleaned_data['password1']
                    )

                    return HttpResponseRedirect(reverse('login:login'))
                else:
                    return render(request, 'login/mysignupview.html', {
                        'form': SignUpForm(),
                        'error_message': 'Password mismatch. Please confirm password!'
                    })
            else:
                return render(request, 'login/mysignupview.html', {
                    'form': SignUpForm(),
                    'error_message': 'This email is already registered',
                })
