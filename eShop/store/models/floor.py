from django.db import models

class Floor(models.Model):
    """
    Model for each floor of the warehouse/mall
    """
    CHOICES = {1: 'ground floor', 2: 'first floor', 3: 'second floor', 4: 'third floor'}

    level = models.PositiveIntegerField(
        choices=CHOICES,
        primary_key=True,
        db_comment='Floor space storey level',
        help_text='Please enter a positive integer value for the storey level of this floor'
    )

    def __str__(self):
        for k, v in self.CHOICES.items():
            fl = False
            if self.level != k:
                pass
            else:
                fl=v
                break
        if fl:
            return fl
        else:
            return f'Invalid floor level'

    