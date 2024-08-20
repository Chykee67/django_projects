from django.db import models

from login.models import User
from store.models import Item


class UserCart(models.Model):

    """ Model for user cart """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f"{self.user}'s cart"
    
    @classmethod
    def add_to_cart(cls, user, item):
        return cls(
            user=User.objects.get(user_name=user),
            item=Item.objects.get(description=item)
            )

    
    #try to use generatedfield from django.models here to calculate the total worth of items in the cart

#try to use classmethods, static methods and instance methods here
    