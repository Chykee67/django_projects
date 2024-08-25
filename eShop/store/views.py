import emoji

from django.shortcuts import render

from login.models import User
from .models import Category, Subcategory, Item


def IndexView(request, user_name):

    categories = Category.objects.all()

    try:
        user = User.objects.get(user_name=user_name)
    except(KeyError, User.DoesNotExist):
        return render(request, 'store/user_index.html', IndexViewContext(user_name))

    else:
        if user.user_name == 'chykee67':
            return render(request, 'store/admin_index.html', IndexViewContext(user_name))

        else:
            return render(request, 'store/user_index.html', IndexViewContext(user_name))

def IndexViewContext(user_name):
    try:
        user = User.objects.get(user_name=user_name)
    except (KeyError, User.DoesNotExist):
        return {
            'cheers': emoji.emojize(":party_popper:"),
            'categories': Category.objects.all(),
        }
    else:
        return {
            'user': user,
            'cheers': emoji.emojize(":party_popper:"),
            'categories': Category.objects.all(),
        }

# Create your views here.
