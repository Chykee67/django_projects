from django.contrib.auth.models import models, Permission, Group
from login.models import User

class Adults(Group):
    """
    A GROUP FOR USERS OVER THE AGE OF 18
    """

    users = models.ManyToManyField(User)
