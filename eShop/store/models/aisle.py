from django.db import models

from .section import Section

class Aisle(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        help_text="Mall section where rack is found",
    )

    id = models.CharField(
        max_length=5,
        primary_key=True,
        help_text="Aisle's unique ID",
        verbose_name='Aisle ID',
    )

    description = models.CharField(
        max_length=100,
        help_text="Items on this aisle",
        default="items"
    )

    aisles = models.Manager()

    def __str__(self):
        return self.id