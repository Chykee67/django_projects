from django.db import models

class Tag(models.Model):
    description = models.CharField(
        max_length=15,
        verbose_name="tag",
        help_text="Item tags",
        primary_key=True,
    )

    tags = models.Manager()

    def __str__(self):
        return self.description