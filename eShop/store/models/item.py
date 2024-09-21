from django.db import models

from .aisle import Aisle
from .section import Section


class Item(models.Model):
    aisle = models.ForeignKey(
        Aisle,
        on_delete=models.CASCADE,
        help_text="Aisle where item is displayed"
    )

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        help_text="Mall Section",
    )

    title = models.CharField(
        max_length=100,
        primary_key=True,
        verbose_name="Item title",
        help_text="Title of item for sale",
    )

    price = models.PositiveIntegerField(
        help_text="Price of item in Naira",
        verbose_name="Selling price",
    )

    cost = models.PositiveIntegerField(
        help_text="Cost of Item in Naira",
        verbose_name="Cost price"
    )

    def profit_margin(self):
        return self.cost - self.price

    def __str__(self):
        return self.title