from django.db import models

from .aisle import Aisle
from .section import Section
from .tag import Tag


class TaggedItemsQuerySet(models.QuerySet):
    """
    Custom QuerySets for tagged items
    """

    def itemslist(self, tag: str):
        return self.filter(tags=tag)

class TaggedItemsManager(models.Manager):
    """
    Custom manager for tagged items
    """

    def get_queryset(self):
        return TaggedItemsQuerySet(self.model, using=self._db)

    def itemslist(self, tag: str):
        return self.get_queryset().itemslist(tag)


class Item(models.Model):
    aisle = models.ForeignKey(
        Aisle,
        on_delete=models.CASCADE,
        help_text="Aisle where item is displayed",
        default='AA000',
    )

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        help_text="Mall Section",
        default='section',
    )

    description = models.CharField(
        max_length=100,
        primary_key=True,
        verbose_name="Item title",
        help_text="Title of item for sale",
        default='item',
    )

    price = models.PositiveIntegerField(
        help_text="Price of item in Naira",
        verbose_name="Selling price",
        default=0,
    )

    cost = models.PositiveIntegerField(
        help_text="Cost of Item in Naira",
        verbose_name="Cost price",
        default=0,
    )

    tags = models.ManyToManyField(
        Tag,
    )

    trend = models.IntegerField(
        default=0,
    )

    items = models.Manager()
    tagged = TaggedItemsManager()

    def profit_margin(self):
        return self.cost - self.price

    def __str__(self):
        return self.description