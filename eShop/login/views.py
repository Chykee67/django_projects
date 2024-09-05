from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


from .forms import SignInForm, SignUpForm
from .models import User


def SignIn(request):

    """ View for collecting user input. """

    return render(request, 'login/signin.html', {'form': SignInForm()})

def AuthoriseUser(request):

    """ Function for validating user input on sign in page. """

    if request.method == "POST":
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
                    'form': form,
                    'error_message': 'Incorrect email or password'
                })
        else:
            return HttpResponse('Invalid Form')
    else:
        return HttpResponse('Invalid request method')

def LogOutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:sign_in'))



    # handle obejctDoesNotExistError if not previously registered


def SignUp(request):

    """ View for adding a new user profile. """

    return render(request, 'login/signup.html', {'form': SignUpForm()})

    # raise my ValueError if conditions not met for provided user_name and password
    ...

def CreateUser(request):

    """ Function that takes Sign up input and creates a user profile. """

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            new_user = User(
                user_name = form.cleaned_data['user_name'],
                password = form.cleaned_data['password'],
                user_email = form.cleaned_data['user_email'],
                about_user = form.cleaned_data['about_user'],
                country_of_residence = form.cleaned_data['country_of_residence'],
                state_of_residence = form.cleaned_data['state_of_residence'],
                city_of_residence = form.cleaned_data['city_of_residence'],
                street_address = form.cleaned_data['street_address'],
                )
            
            try:
                registered_user = User.objects.get(user_name=new_user.user_name)
            except (KeyError, User.DoesNotExist):
                new_user.save()
                return HttpResponseRedirect(reverse('usr_profile:profile', args=(new_user,)))
            else:
                return render(request, 'login/signup.html', {
                    'form': SignUpForm(),
                    'error_message': f'User {registered_user} Already Exists!'
                })

        else:
            return render(request, 'login/signup.html', {'form':SignUpForm()})


    else:
        return render(request, 'login/signup.html', {'form':SignUpForm()})
    
    # raise user_name Exists Error, email attached to another account
    # raise weak password error

    
# Create your views here.
