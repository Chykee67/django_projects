from django.db import models

from .item import Item

class Stock(models.Model):
    """
    Store inventory model
    """

    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        help_text="amount in store",
        verbose_name="Stored quantity",
        default=0,
    )

    stocks = models.Manager()

    def __str__(self):
        return f"{self.item.description}: {self.quantity}"