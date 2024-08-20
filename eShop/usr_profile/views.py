from django.shortcuts import render
from django.http import HttpResponse


from login.models import User
from store.models import Category, Subcategory, Item
from .models import UserItem, Order



def Index(request, user_name):

    """ View for user profile index page """

    cart = UserItem.objects.filter(user__user_name=user_name)

    orders = Order.objects.filter(user__user_name=user_name)

    return render(request, 'usr_profile/index.html',{})


# Create your views here.
