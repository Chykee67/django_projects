from django.db import models
from django.utils import timezone

from login.models import User
from store.models import Item

class Order(models.Model):
    """
    Model for a registered user's Order
    """

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
    )

    item = models.OneToOneField(
        Item,
        on_delete=models.PROTECT,
    )

    unit = models.CharField(
        max_length=100,
    )

    quantity = models.PositiveIntegerField()

    per_unit_charge = models.PositiveIntegerField()

    discount = models.PositiveIntegerField(
        default=0,
    )

    def charge(self):
        return (self.per_unit_charge * self.quantity) - self.discount

    def __str__(self):
        return f"{self.item}: {self.charge()}"