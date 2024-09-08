import countryflag

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_not_required

from login.models import User
from store.models import Category, Subcategory, Item
from .models import UserItem, Order, Notification



def Index(request, user_first_name):

    """ View for user profile index page """

    user = get_object_or_404(User, first_name=user_first_name)

    if user.country_of_residence:
        flag = countryflag.getflag([user.country_of_residence])

        return render(request, 'usr_profile/index.html', {
            'user': user,
            'flag': flag,
            'notification_count': get_notification_count(),
        })
    else:
        return render(request, 'usr_profile/index.html', {
            'user': user,
            'notification_count': get_notification_count(),
        })

class CartView(ListView):

    """ A View of User Cart """

    def get(self, request, user_name):

        user = get_object_or_404(User, first_name=user_name)

        return render(request, 'usr_profile/cartview.html', {
            'cart': UserItem.objects.filter(user=user),
            'user': user,
        })
    
    


def OrdersView(request, user_name):

    """ A View for the User's orders """

    orders = Order.objects.filter(user__user_name=user_name)


    return render(request, 'usr_profile/orders.html', {
        'orders': orders,
        'user_name': user_name
    })

def Notifications(request, user_first_name):

    """ View for messages and notifications for the user """

    return render(request, 'usr_profile/notifications.html', {
        'notification_count': get_notification_count(),
        'notifications': Notification.objects.all(),
    })

def get_notification_count():
    notification_counter = 0

    if Notification.objects.all() != []:
        for notification in Notification.objects.all():
            notification_counter+=1
    else: pass

    return notification_counter
# Create your views here.
