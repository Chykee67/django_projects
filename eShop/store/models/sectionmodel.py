from django.db import models

from .floormodel import Floor
from .tagmodel import Tag

class Section(models.Model):
    floor = models.ForeignKey(
        Floor,
        on_delete=models.CASCADE,
        help_text="Floor where section can be found",
    )

    description = models.CharField(
        max_length=100,
        primary_key=True,
        help_text="Title of mall section",
        verbose_name="Section",
    )

    tags = models.ManyToManyField(Tag)

    trend = models.IntegerField(
        default=0,
    )

    sections = models.Manager()

    def __str__(self):
        return self.description