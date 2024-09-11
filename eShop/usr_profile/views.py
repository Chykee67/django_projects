import countryflag

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.list import ListView

from login.models import User
from login.forms import EditUserProfileForm
from store.models import Category, Subcategory, Item
from .models import UserItem, Order, Notification



class IndexView(View):

    http_method_names = ["get", "head", "options", "trace"]

    def get(self, request, user_first_name):

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


class EditUserProfile(View):

    def get(self, request, user_first_name):

        return render(request, 'usr_profile/edit_user_profile.html', {
            'form': EditUserProfileForm(),
            'user': User.objects.get(first_name=user_first_name)
        })

    def post(self, request, user_first_name):

        user = User.objects.get(first_name=user_first_name)

        form = EditUserProfileForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['first_name'] != '':
                user.first_name = form.cleaned_data['first_name']
            else: pass
            if form.cleaned_data['last_name'] != '':
                user.last_name = form.cleaned_data['last_name']
            else: pass
            if form.cleaned_data['date_of_birth'] != '1970-01-01':
                user.date_of_birth = form.cleaned_data['date_of_birth']
            else: pass
            if form.cleaned_data['about_user'] != '':
                user.about_user = form.cleaned_data['about_user']
            else: pass
            if form.cleaned_data['country_of_residence'] != '':
                user.country_of_residence = form.cleaned_data['country_of_residence']
            else: pass
            if form.cleaned_data['state_of_residence'] != '':
                user.state_of_residence = form.cleaned_data['state_of_residence']
            else: pass
            if form.cleaned_data['city_of_residence'] != '':
                user.city_of_residence = form.cleaned_data['city_of_residence']
            else: pass
            if form.cleaned_data['street_address'] != '':
                user.street_address = form.cleaned_data['street_address']
            else: pass

            user.save()

            return HttpResponseRedirect(reverse('usr_profile:index', args=(user,)))
        else:
            return HttpResponse(f'{form.errors}')
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
