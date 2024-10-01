from django.db import models

from login.models import User
from store.models import Item

class Cart(models.Model):
    """
    Model for a registered user's cart
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    item = models.ManyToManyField(
        Item,
    )

    carts = models.Manager()

    def __str__(self):
        return f"{self.user}'s cart"