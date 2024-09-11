from datetime import timedelta

from django.db import models
from django.utils import timezone

from login.models import User
from store.models import Item


class UserItem(models.Model):

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
        return self.item.description
    
    @classmethod
    def add_to_cart(cls, user, item):
        return cls(
            user=User.objects.get(user_name=user),
            item=Item.objects.get(description=item)
            )


class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField()
    
    order_creation_date = models.DateTimeField(
        timezone.now(),
    )

    expected_delivery_date = models.DateTimeField(
        timezone.now() + timedelta(days=7)
    )


class Notification(models.Model):

    subject = models.CharField(
        max_length = 40,
        default='New Notification',
    )

    message = models.TextField(
        max_length = 300,
    )

    message_sent_date = models.DateTimeField(timezone.now())


    def __str__(self):
        return self.message


    #try to use generatedfield from django.models here to calculate the total worth of items in the cart

#try to use classmethods, static methods and instance methods here
    