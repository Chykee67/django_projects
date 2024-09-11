from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required
from django.views import View


from .forms import SignInForm, SignUpForm, ForgottenPasswordForm
from .models import User


@method_decorator(login_not_required, name="dispatch")
class myloginView(View):

    def get(self, request):
        return render(request, 'login/signin.html', {
            'form': SignInForm(),
        })

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('usr_profile:index', args=(user,)))
            else:
                return render(request, 'login/signin.html', {
                    'form': SignInForm(),
                    'error_message': 'Incorrect email or password',
                })
        else:
            return HttpResponse(f'{form.errors}')

@method_decorator(login_not_required, name="dispatch")
class PasswordResetView(View):

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



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login:login'))


@method_decorator(login_not_required, name="dispatch")
class SignUpView(View):
    def get(self, request):
        return render(request, 'login/signup.html', {
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

                    return HttpResponseRedirect(reverse('usr_profile:index', args=(new_user,)))
                else:
                    return render(request, 'login/signup.html', {
                        'form': SignUpForm(),
                        'error_message': 'Password mismatch. Please confirm password!'
                    })
            else:
                return render(request, 'login/signup.html', {
                    'form': SignUpForm(),
                    'error_message': 'This email is already registered',
                })

