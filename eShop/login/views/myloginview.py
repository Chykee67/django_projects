from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_not_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from login.forms import SignInForm


@method_decorator(login_not_required, name="dispatch")
class MyLoginView(View):

    def get(self, request):
        return render(request, 'login/signin.html', {
            'form': SignInForm(),
            'session_user': request.session.get('user', False),
        })

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login/signin.html', {
                    'form': SignInForm(),
                    'error_message': 'Incorrect email or password',
                })
        else:
            return HttpResponse(f'{form.errors}')
