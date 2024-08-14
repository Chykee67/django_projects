from django.shortcuts import render
from django.http import HttpResponse

from login.models import User

def Index(request, user_name):
    return render(request, 'usr_profile/index.html')

def UserCart(request, user_name):

    user = User.objects.get(user_name=user_name)

    return render(request, 'usr_profile:view_cart.html', {
        'Cart': Cart,
        'user': user,
    })

# Create your views here.
