from django.db import models
from django.utils import timezone

from login.models import User

class Notification(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    subject = models.CharField(
        max_length=100,
        verbose_name="Notification Subject",
    )

    body = models.TextField(
        verbose_name="Notification Message",
    )

    sent_date = models.DateTimeField(
        default=timezone.now,
    )