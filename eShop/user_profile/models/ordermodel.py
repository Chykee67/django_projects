from django.db import models
from django.utils import timezone

from login.models import User
from store.models import Item


class OrderQuerySet(models.QuerySet):
    def pending(self):
        return self.filter(is_pending=True)

    def paid_for(self):
        return self.filter(is_paid_for=True)

    def delivered(self):
        return self.filter(is_delivered=True)


class OrderManager(models.Manager):

    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def pending(self):
        return self.get_queryset().pending()

    def paid_for(self):
        self.get_queryset().paid_for()

    def delivered(self):
        self.get_queryset().delivered()


class Order(models.Model):
    """
    Model for a registered user's Order
    """

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )

    item = models.ForeignKey(
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

    date = models.DateTimeField(
        default=timezone.now,
    )

    is_pending = models.BooleanField(default=True)

    is_paid_for = models.BooleanField(default=False)

    is_delivered = models.BooleanField(default=False)

    orders = OrderManager()

    def charge(self):
        return (self.per_unit_charge * self.quantity) - self.discount

    def status(self):
        if self.is_pending:
            return "Pending"
        elif self.is_paid_for and not self.is_delivered:
            return "Awaiting Delivery"
        elif self.is_paid_for and self.is_delivered:
            return "Delivered"
        else:
            return "Uncertain"

    def __str__(self):
        return f"{self.item} {self.unit}x{self.quantity}: {self.charge()}"