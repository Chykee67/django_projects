from django.db import models

from .floor import Floor

class Section(models.Model):
    floor = models.ForeignKey(
        Floor,
        on_delete=models.CASCADE,
        help_text="Floor where section can be found",
    )

    title = models.CharField(
        max_length=100,
        primary_key=True,
        help_text="Title of mall section",
        verbose_name="Section",
    )