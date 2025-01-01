from django.db import models

from .aislemodel import Aisle
from .sectionmodel import Section
from .tagmodel import Tag


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

    info = models.TextField(
        verbose_name ='Item Info',
        help_text='more info on the item',
        default='add item info here',
    )

    retail_unit = models.CharField(
        help_text="retailing unit",
        max_length=40,
        default="1 piece",
    )

    retail_unit_price = models.PositiveIntegerField(
        help_text="Price of 1 retail unit in Naira",
        verbose_name="Retail price",
        default=0,
    )

    wholesale_unit = models.CharField(
        help_text="unit for wholesale",
        max_length=40,
        default="1 pack",
    )

    wholesale_unit_price = models.PositiveIntegerField(
        help_text="Price of 1 wholesale unit in Naira",
        verbose_name="Wholesale price",
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