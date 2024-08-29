

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager



class User(AbstractUser):
    username = models.CharField(
        max_length = 40,
        unique=True,
    )

    first_name = models.CharField(
        max_length = 40,
    )

    last_name = models.CharField(
        max_length=40,
    )

    email = models.EmailField(
        max_length=40,
    )

    date_of_birth = models.DateField()

    about_user = models.TextField(
        max_length=300,
        blank=True,
    )
    country_of_residence = models.CharField(
        max_length=100,
        blank=True,
        )
    state_of_residence = models.CharField(
        max_length=100,
        blank=True,
        )
    city_of_residence = models.CharField(
        max_length=100,
        blank=True,
        )
    street_address = models.TextField(
        max_length=300,
        blank=True,
        )

    USERNAME_FIELD = "username"

    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = [
        "email",
        "date_of_birth",
        "country_of_residence",
        "state_of_residence",
        "city_of_residence",
        "street_address",
        "first_name",
        "last_name",
    ]

    #is_active=True

    def get_full_name():
        return f"{self.first_name}, {self.last_name}"

    def get_short_name():
        return f"{self.first_name}"

    def __str__(self):
        return self.username

class CustomUserManager(BaseUserManager):

    """ Manager for User model above """

    def create_user(
        self,
        username,
        email,
        date_of_birth,
        country_of_residence,
        state_of_residence,
        city_of_residence,
        street_address,
        first_name,
        last_name,
        password=None,
    )

        return User(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            country_of_residence=country_of_residence,
            state_of_residence=state_of_residence,
            city_of_residence=city_of_residence,
            street_address=street_address,
            first_name=first_name,
            last_name=last_name,
        )

        #stopped at page 583